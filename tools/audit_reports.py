#!/usr/bin/env python3
"""Render typed priority and algorithmic records without changing source evidence."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def write(d):
 s={v['id']:v for v in d['sources']};ls=['# Source priority and version audit','','Specific reconciliations, not a complete first-attribution inventory. Source checks are statement/normalization/proof-route checks, not independent certification.','']
 for v in d.get('priority_audits',[]):ls+=['## '+v['id'],'',v['finding'],'','Sources: '+', '.join('['+id+']('+s[id]['url']+')' for id in v['sources'])+'. Status: '+v['status']+'.','']
 for v in d.get('literature_searches',[]):ls+=['## Targeted search: '+v['id'],'',v['conclusion'],'','Queries: '+ '; '.join(v['queries'])+'.','']
 (ROOT/'docs/priority-audit.md').write_text('\n'.join(ls)+'\n')
 ls=['# Typed algorithmic bounds, reductions and problem classes','','These statements have parameters or change objects/models; they are not silently entered as scalar function-measure inequalities.','']
 for v in d.get('reductions',[]):ls+=['## '+v['id'],'',v['construction'],'',v['proof_summary'],'',*['- '+b for b in v['bounds']],'',v['notes'],'', 'Source: ['+v['source']+']('+s[v['source']]['url']+'), '+v['locator']+'.','']
 for v in d.get('algorithmic_bounds',[]):ls+=['## '+v['id'],'',v['statement'],'',v['proof_summary'],'',v['notes'],'','Source: ['+v['source']+']('+s[v['source']]['url']+'), '+v['locator']+'.','']
 for v in d.get('problem_classes',[]):ls+=['## '+v['id'],'',v['definition'],'',v['scalar_characterization'],'',v['notes'],'','Source: ['+v['source']+']('+s[v['source']]['url']+'), '+v['locator']+'.','']
 (ROOT/'docs/model-transformations.md').write_text('\n'.join(ls)+'\n');print('Generated priority, search-status and typed model reports.')
if __name__=='__main__':write(json.loads((ROOT/'data/catalog.json').read_text()))
