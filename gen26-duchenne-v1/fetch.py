"""Retéléchargement optionnel borné ; analyse hors ligne possible avec les fichiers livrés."""
import argparse, gzip, hashlib, json, urllib.request
from pathlib import Path
URLS={
'GSE38417_series_matrix.txt.gz':('https://ftp.ncbi.nlm.nih.gov/geo/series/GSE38nnn/GSE38417/matrix/GSE38417_series_matrix.txt.gz',10000000,False),
'GPL570.soft.gz':('https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL570&targ=self&form=text&view=full',100000000,True)}
a=argparse.ArgumentParser();a.add_argument('--out',required=True,type=Path);o=a.parse_args().out;o.mkdir(parents=True,exist_ok=False)
log=[]
for name,(url,limit,compress) in URLS.items():
    with urllib.request.urlopen(url,timeout=45) as r:
        length=r.headers.get('Content-Length')
        if length and int(length)>limit: raise ValueError('Content-Length au-delà du plafond')
        content=r.read(limit+1)
        if len(content)>limit: raise ValueError('Réponse au-delà du plafond')
    if compress:
        if not content.rstrip().endswith(b'!platform_table_end'): raise ValueError('Table incomplète / HTML inattendu')
        with (o/name).open('wb') as f:
            with gzip.GzipFile(fileobj=f,mode='wb',mtime=0) as g:g.write(content)
    else:
        if b'!series_matrix_table_end' not in gzip.decompress(content): raise ValueError('Matrice incomplète')
        (o/name).write_bytes(content)
    log.append(dict(url=url,received_bytes=len(content),file=name,sha256=hashlib.sha256((o/name).read_bytes()).hexdigest()))
(o/'downloads.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps(log,indent=2))
