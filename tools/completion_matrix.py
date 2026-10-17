#!/usr/bin/env python3
"""Lift upper-bound chains through minimum over total Boolean completions."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def build(core):
 scope=dict(object_kind='decision_function',totality='partial_or_total',classes=[],input_alphabet='bits',output_alphabet='bits',cost='as_in_measure_definitions',error='as_in_measure_definitions',assumptions=[])
 rows=[]
 for cell in core['cells']:
  if cell['A']==cell['B']:continue
  rows.append(dict(A='completion_'+cell['A'],B='completion_'+cell['B'],base_A=cell['A'],base_B=cell['B'],upper=copy.deepcopy(cell['upper']),lower=copy.deepcopy(cell['lower']),lower_justification='On a total function the only total completion is the function itself. The recorded total witness therefore witnesses the same lower exponent for the completion measures.',source='HKMP26',locator='Definition 45 and Observation 47',proof='Choose F_B attaining min B. Then min A<=A(F_B)<=g(B(F_B))=g(min B). Apply the recorded total-function upper chain.',scope=scope,status='repository_lifting_derivation',globally_best_known_certified=False,warning='Upper bounds use the minimizing-completion argument; lower witnesses transfer separately because completion measures equal their base measures on total functions. Preserve logarithmic endpoint losses. No arbitrary completion is asserted optimal for both measures.'))
 return dict(order=['completion_'+m for m in core['order']],scope=scope,cells=rows,inference_policy='Lift recorded total-core upper chains; no new priority or best-known certification.')
def main():
 out=build(json.loads((ROOT/'data/core-matrix.json').read_text()));(ROOT/'data/completion-matrix.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 ls=['# Minimum-completion exponent bounds','',out['inference_policy'],'','For every pair choose the completion optimal for the right-hand measure. The minima may use different completions. Native promise measures are not substituted for minimum-completion measures.','', '| A | B | Lower exponent | Upper exponent | Pure endpoint? | Base claim chain |','|---|---|---:|---:|---|---|']
 for c in out['cells']:
  u=c['upper'];ls.append('| '+c['A']+' | '+c['B']+' | '+str(c['lower']['exponent_expression'])+' | '+str(u['exponent'])+' | '+('yes'if u['endpoint_without_log']else'no: retain logarithmic loss')+' | '+', '.join(u['claim_ids'])+' |')
 (ROOT/'docs/completion-matrix.md').write_text('\n'.join(ls)+'\n');print('Generated 132 completion upper-bound chains.')
if __name__=='__main__':main()
