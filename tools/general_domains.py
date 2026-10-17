#!/usr/bin/env python3
"""Render pinned query-domain profiles without inferring parameter-free bounds."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 d=json.loads((ROOT/'data/general-domains.json').read_text());ls=['# Query domains and their parameters','','Sources: DFLLV22author, '+d['definition_locators']+'; corresponding definitions and selected bounds checked in final journal DFLLV26 (60 article pages).' ,'',*['- '+w for w in d['warnings']],'','## Definitions','']
 for k,v in d['parameters'].items():ls+=['- **'+k+'**: '+v]
 ls+=['','## Domain profiles','','| Domain | Query | c | Delta | M | beta | beta_c | alpha |','|---|---|---:|---|---|---|---|---|']
 for p in d['profiles']:ls.append('| '+p['domain'].replace('|','\\|')+' | '+p['queries']+' | '+' | '.join(str(p[k]).replace('|','\\|')for k in ['chunk','Delta','M','beta','beta_c','alpha'])+' |')
 ls+=['','The same underlying set can have different query families. S_n with both forward and inverse queries is different from the all-distinct multislice with forward-only coordinate queries. The latter can have linear deterministic complexity at degree one.','']
 for p in d['profiles']:
  if p.get('caveat'):ls+=['- '+p['domain']+': '+p['caveat']]
 (ROOT/'docs/general-domains.md').write_text('\n'.join(ls)+'\n')
if __name__=='__main__':main()
