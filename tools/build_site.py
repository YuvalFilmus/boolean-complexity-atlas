#!/usr/bin/env python3
"""Build the dependency-free GitHub Pages site from the audited plaintext catalogue."""
import json, shutil, sys
import witness_gallery
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from matrix import expr_value, expr_text

def build():
    dst=ROOT/'_site'
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(ROOT/'site',dst)
    (dst/'data').mkdir()
    catalog=json.loads((ROOT/'data/catalog.json').read_text())
    latex=json.loads((ROOT/'data/statement-latex.json').read_text())['statements']
    for c in catalog['claims']:
        if c['id'] in latex: c['statement_latex']=latex[c['id']]
        e=c.get('exponent_expression',c.get('exponent'))
        if e is not None:
            try: c['exponent_numeric']=expr_value(e);c['exponent_label']=expr_text(e)
            except (ValueError,TypeError,KeyError,ZeroDivisionError): pass
    datasets={}
    for key,name in [('total','core-matrix'),('partial','partial-matrix'),('completion','extended-completion-exponents'),('search','search-matrices'),('profiles','profile-matrices'),('permutation','permutation-matrix'),('domains','domain-matrix')]:
        datasets[key]=json.loads((ROOT/'data'/(name+'.json')).read_text())
    for key in ['total','partial','completion']:
        for c in datasets[key]['cells']:
            lo=c.get('lower')
            if lo and 'exponent_expression' in lo: lo['expression_label']=expr_text(lo['exponent_expression'])
    gallery=witness_gallery.build(catalog,json.loads((ROOT/'data/witness-constructions.json').read_text()))
    payload={'gallery':gallery,'campaign':json.loads((ROOT/'data/sensitivity-campaign.json').read_text()),'catalog':catalog,'datasets':datasets,'journal_versions':json.loads((ROOT/'data/journal-version-audit.json').read_text()),'notation':json.loads((ROOT/'data/notation-register.json').read_text())}
    (dst/'data/atlas.json').write_text(json.dumps(payload,ensure_ascii=False,separators=(',',':'))+'\n')
    shutil.copy2(ROOT/'bibliography.bib',dst/'bibliography.bib')
    shutil.copytree(ROOT/'data',dst/'downloads')
    (dst/'downloads/separation-gallery.json').write_text(json.dumps(gallery,ensure_ascii=False,indent=2)+'\n')
    shutil.copytree(ROOT/'docs',dst/'research-notes')
    (dst/'downloads/README.txt').write_text('Authoritative plaintext catalogue: catalog.json. Generated matrices retain provenance and endpoint conventions. Source PDFs are not redistributed. The research notes are available under ../research-notes/.\n')
    (dst/'.nojekyll').write_text('')
    print(f'Built {dst}: {len(catalog["measures"])} measures, {len(catalog["claims"])} claims, {len(catalog["sources"])} references.')
if __name__=='__main__': build()
