#!/usr/bin/env python3
"""Upper-bound closure for domain-qualified S_n measures; never Boolean-cube edges."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ORDER=['permD','permRfail23','permR','permC','permUC','permFBS','permBS','permS','permDegree','permAdeg','permQE','permQ']
def build(d):
 paths={(a,a):(Fraction(1),[])for a in ORDER}
 for c in d['claims']:
  if c['kind']!='upper_bound'or not c.get('scalar_inference_allowed')or c['exponent']is None:continue
  if c['scope']['input_alphabet']!='permutation'or c['scope']['classes']!=['symmetric_group']:continue
  a,b=c['A'],c['B']
  if a not in ORDER or b not in ORDER:continue
  v=Fraction(str(c['exponent']))
  if (a,b)not in paths or v<paths[a,b][0]:paths[a,b]=(v,[c['id']])
 for k in ORDER:
  for a in ORDER:
   for b in ORDER:
    if (a,k)in paths and(k,b)in paths:
     v=paths[a,k][0]*paths[k,b][0]
     if(a,b)not in paths or v<paths[a,b][0]:paths[a,b]=(v,paths[a,k][1]+paths[k,b][1])
 return dict(order=ORDER,warning='Derived upper exponents from indexed S_n claims only. Not best-known certification; no lower-bound optimality is asserted. Symbol queries allow forward and inverse values. Edge sensitivity t is excluded from this polynomial-equivalence matrix.',cells=[dict(A=a,B=b,upper_exponent=str(paths[a,b][0])if(a,b)in paths else None,claim_ids=paths[a,b][1]if(a,b)in paths else [],globally_best_known_certified=False)for a in ORDER for b in ORDER if a!=b])
def main():
 out=build(json.loads((ROOT/'data/catalog.json').read_text()));(ROOT/'data/permutation-matrix.json').write_text(json.dumps(out,indent=2)+'\n');ls=['# Symmetric-group upper-bound matrix','',out['warning'],'','| A | B | Upper exponent | Claim chain |','|---|---|---:|---|']
 for c in out['cells']:ls.append('| '+c['A']+' | '+c['B']+' | '+str(c['upper_exponent'])+' | '+', '.join(c['claim_ids'])+' |')
 (ROOT/'docs/permutation-matrix.md').write_text('\n'.join(ls)+'\n');print('Generated S_n upper chains:',sum(c['upper_exponent']is not None for c in out['cells']),'/132')
if __name__=='__main__':main()
