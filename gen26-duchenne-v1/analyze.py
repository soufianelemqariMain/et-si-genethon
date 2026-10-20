"""Analyse descriptive des fichiers GEO déposés ; bibliothèque standard uniquement."""
import argparse, csv, gzip, hashlib, json, math, platform, resource, statistics, time
from pathlib import Path
ROOT = Path(__file__).resolve().parent
TARGETS = {'LTBP4','THBS1','SPP1'}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def analyze(data):
    mapping={}; inside=False; ended=False; annotation_rows=0
    with gzip.open(data/'GPL570.soft.gz','rt') as f:
        for line in f:
            if line.startswith('!platform_table_begin'): inside=True; header=next(f).rstrip('\n').split('\t'); continue
            if line.startswith('!platform_table_end'): ended=True; break
            if inside:
                row=dict(zip(header,line.rstrip('\n').split('\t'))); annotation_rows+=1
                if row['Gene Symbol'] in TARGETS:
                    assert row['ID'] not in mapping
                    mapping[row['ID']]=row['Gene Symbol']
    assert ended and annotation_rows>50000 and set(mapping.values())==TARGETS
    meta={}; rows=[]; ended=False; seen=set(); total=0
    with gzip.open(data/'GSE38417_series_matrix.txt.gz','rt') as f:
        for line in f:
            cells=next(csv.reader([line],delimiter='\t'))
            if not cells: continue
            if cells[0].startswith('!Sample_'): meta.setdefault(cells[0],[]).append(cells[1:])
            if cells[0]=='ID_REF': samples=cells[1:]; continue
            if cells[0]=='!series_matrix_table_end': ended=True; break
            if cells[0].startswith('!') or not cells[0]: continue
            assert len(cells)==len(samples)+1
            assert cells[0] not in seen;seen.add(cells[0]);total+=1
            if cells[0] in mapping:
                values=[float(v) for v in cells[1:]]
                assert all(math.isfinite(v) for v in values)
                rows.append((cells[0],mapping[cells[0]],values))
    assert ended and len(samples)==len(set(samples))==22 and set(mapping)<=seen
    groups=meta['!Sample_source_name_ch1'][0]
    assert set(groups)=={'control_muscle biopsy','DMD_muscle biopsy'}
    assert meta['!Sample_geo_accession'][0]==samples
    contrasts=[]; selected=[]
    for probe,gene,values in sorted(rows):
        a=[v for v,g in zip(values,groups) if g=='DMD_muscle biopsy']
        b=[v for v,g in zip(values,groups) if g=='control_muscle biopsy']
        assert len(a)==16 and len(b)==6
        contrasts.append(dict(probe=probe,gene=gene,n_dmd=len(a),n_control=len(b),median_dmd=statistics.median(a),median_control=statistics.median(b),delta_medians=statistics.median(a)-statistics.median(b),min_dmd=min(a),max_dmd=max(a),min_control=min(b),max_control=max(b)))
        selected.extend(dict(sample=s,group=g,probe=probe,gene=gene,value=v) for s,g,v in zip(samples,groups,values))
    sensitivity=[]
    for row in csv.DictReader((data/'weiss2018_table1.csv').open()):
        for cohort in ['n253','n243','n189']:
            p=float(row[cohort]);assert 0<p<=1
            sensitivity.append(dict(snp=row['snp'],gene=row['gene'],cohort=cohort,p=p,passes_5e_8=p<5e-8,minus_log10_p=-math.log10(p)))
    return dict(matrix_rows=total,annotation_rows=annotation_rows,selected_probes=len(rows),sample_count=len(samples),metadata=meta,contrasts=contrasts,selected_values=selected,sensitivity=sensitivity,input_sha256={p.name:digest(p) for p in sorted(data.iterdir()) if p.is_file()})
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data',type=Path,default=ROOT/'data');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    a.out.mkdir(parents=True,exist_ok=False)
    start=time.perf_counter();cpu=time.process_time();r=analyze(a.data)
    (a.out/'results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    for name in ['contrasts','selected_values','sensitivity']:
        with (a.out/(name+'.csv')).open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(r[name][0]));w.writeheader();w.writerows(r[name])
    usage=resource.getrusage(resource.RUSAGE_SELF)
    measure=dict(python=platform.python_version(),platform=platform.platform(),machine=platform.machine(),wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,max_rss_raw=usage.ru_maxrss,max_rss_unit='bytes' if platform.system()=='Darwin' else 'KiB',scope='processus analyse seulement ; réseau et inférence distante exclus')
    (a.out/'execution.json').write_text(json.dumps(measure,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ['sample_count','matrix_rows','annotation_rows','selected_probes']}))
if __name__=='__main__':main()
