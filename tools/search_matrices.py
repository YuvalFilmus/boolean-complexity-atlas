#!/usr/bin/env python3
"""Scope-separated, direct-evidence inventories for search measures; no closure."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NODES=['D','R0','Rfail','R','Q','QE','rel_Qeps','psR','psQ','rel_deg','rel_udeg','rel_adeg','rel_conical','rel_bs','rel_fbs','rel_cbs','rel_fcbs','rel_Adv','rel_CAdv','V']
SIZE=['DTSize','DTNodes','RSize','RNodes','psDTSize','Ddist','DSizeDist','Dna','Rna','psRna']
def build(d):
 out=[]
 for totality in ['total','partial']:
  for label,nodes in [('query_and_lower_bounds',NODES),('size_distribution_nonadaptivity',SIZE),('average_cost',['Davg','Ravg','R0avg','psRavg','psR0avg']),('restricted_query_oracles',['DandPos','RandPos','psRandPos','DandOr','RandOr','psRandOr','DzeroDepth','RzeroDepth','Dpar','Rpar','psRpar'])]:
   cells=[]
   for a in nodes:
    for b in nodes:
     cs=[c for c in d['claims'] if c['A']==a and c['B']==b and c['scope']['object_kind']=='search_relation' and c['scope']['totality'] in [totality,'partial_or_total']]
     cells.append(dict(A=a,B=b,records=[dict(claim_id=c['id'],scope=c['scope'],kind=c['kind'],historical=bool(c.get('historical')),exponent=c['exponent'],loss=c['loss']) for c in cs],status='direct_evidence_indexed' if cs else 'not_yet_indexed'))
   out.append(dict(totality=totality,group=label,nodes=nodes,cells=cells))
 return dict(warning='Direct evidence inventory, not an optimal-exponent table. Scope restrictions, mixed alphabets, logarithms and historical status remain in every cell. Blank means not yet indexed, not open or incomparable. Distinct groups omit cross-group pairs here; the all-measure pair index retains them.',matrices=out)
def write(d):
 out=build(d);(ROOT/'data/search-matrices.json').write_text(json.dumps(out,indent=2)+'\n')
 ls=['# Search-relation pair inventories','',out['warning'],'','Each number counts claim records for that ordered pair. `—` means not yet indexed. A number does not assert a finite exponent or applicability to all subclasses: follow its claims and scopes.','']
 for mat in out['matrices']:
  ns=mat['nodes'];cells={(v['A'],v['B']):v for v in mat['cells']};ls+=['## '+mat['totality']+' / '+mat['group'],'','| A / B | '+' | '.join(ns)+' |','|---|'+'---|'*len(ns)]
  for a in ns:ls.append('| '+a+' | '+' | '.join(str(len(cells[a,b]['records'])) if cells[a,b]['records'] else '—' for b in ns)+' |')
  ls+=['','Indexed cells:','']
  for v in mat['cells']:
   if v['records']:ls.append('- '+v['A']+' / '+v['B']+': '+', '.join('['+r['claim_id']+'](claims.md#'+r['claim_id']+')' for r in v['records'])+'.')
  ls.append('')
 (ROOT/'docs/search-matrices.md').write_text('\n'.join(ls)+'\n');print('Generated eight search evidence matrices with distinct total/promise domains.')
if __name__=='__main__':write(json.loads((ROOT/'data/catalog.json').read_text()))
