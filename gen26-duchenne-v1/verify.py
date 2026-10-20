"""Vérifie l'intégrité puis reproduit les résultats scientifiques locaux."""
import hashlib,json,subprocess,sys,tempfile
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for name,expected in manifest.items():
    p=root/name
    if hashlib.sha256(p.read_bytes()).hexdigest()!=expected: raise ValueError('Empreinte incorrecte : '+name)
with tempfile.TemporaryDirectory(prefix='gen26-verify-') as t:
    subprocess.run([sys.executable,'-B',str(root/'analyze.py'),'--out',str(Path(t)/'result')],check=True)
    calculated=json.loads((Path(t)/'result/results.json').read_text())
    expected=json.loads((root/'runs/clean-2/results.json').read_text())
    assert calculated==expected,'Résultats différents'
corpus=json.loads((root/'corpus.json').read_text());ids={r['id'] for r in corpus};assert len(ids)==len(corpus)
model=json.loads((root/'model/session-output.json').read_text())
for c in model['candidates']:assert set(c['references'])<=ids
assert len(model['candidates'])>=3
print('PASS: empreintes, reproduction numérique exacte, références modèle autorisées. Pas une validation biologique.')
