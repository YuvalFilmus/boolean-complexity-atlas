#!/usr/bin/env python3
"""Index construction records and every recorded separation, with stable source links."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def build(d,notes):
 claims={c['id']:c for c in d['claims']};sources={s['id']:s for s in d['sources']};entries={};mapping={}
 for w in d.get('witnesses',[]):
  entries[w['id']]={**w,'name':w.get('name',w['id'].replace('-',' ').replace('_',' ')),'claim_ids':list(w.get('claim_ids',[])),'construction_status':w.get('definition_status',w.get('status','source_overview'))}
 for w in notes['constructions']:
  entries[w['id']]={**w,'construction_status':w.get('definition_status','source_overview')}
 for w in entries.values():
  for cid in w['claim_ids']:mapping.setdefault(cid,[]).append(w['id'])
 for c in d['claims']:
  if c.get('witness_id') in entries:
   wid=c['witness_id'];mapping.setdefault(c['id'],[])
   if wid not in mapping[c['id']]:mapping[c['id']].append(wid)
 # Explicit OR-family claims and their source-free consequences share the same construction.
 for c in d['claims']:
  if c['id'].startswith('OR-') and c['kind']=='separation':mapping.setdefault(c['id'],[]).append('OR_n')
 # Derived comparisons inherit construction IDs through explicit dependencies only.
 for _ in range(len(claims)):
  changed=False
  for c in d['claims']:
   if c['kind'] not in ['separation','no_polynomial_bound']:continue
   found=list(dict.fromkeys(mapping.get(c['id'],[])+[w for dep in c.get('depends_on',[]) for w in mapping.get(dep,[])]))
   if found and found!=mapping.get(c['id']):mapping[c['id']]=found;changed=True
  if not changed:break
 # Remaining source witnesses are grouped only when their recorded proof descriptions coincide.
 # Mark definition-extraction limits rather than inventing a missing formal construction.
 for c in d['claims']:
  if c['kind'] not in ['separation','no_polynomial_bound'] or mapping.get(c['id']):continue
  key='source-'+str(c['source'])+'-'+hashlib.sha256(c['proof_summary'].encode()).hexdigest()[:10]
  if key not in entries:
   entries[key]={'id':key,'name':c.get('witness') or c['id'].replace('-',' '),'definition':c['proof_summary'],'proof_summary':c['proof_summary'],'construction_status':'source_proof_overview_full_definition_not_separately_transcribed','notes':'This card indexes the recorded source construction through its checked proof overview and exact reference. A separate full formal definition has not been transcribed.','claim_ids':[]}
  mapping[c['id']]=[key]
 for cid,wids in mapping.items():
  for wid in set(wids):
   if cid not in entries[wid]['claim_ids']:entries[wid]['claim_ids'].append(cid)
 for w in entries.values():
  cs=[claims[cid] for cid in w['claim_ids'] if cid in claims]
  w['claim_ids']=list(dict.fromkeys(w['claim_ids']))
  w['pairs']=[{'A':c['A'],'B':c['B'],'claim_id':c['id'],'kind':c['kind'],'scope':c['scope']} for c in cs if c['kind'] in ['separation','no_polynomial_bound']]
  w['measure_ids']=list(dict.fromkeys(m for c in cs for m in [c.get('A'),c.get('B')] if m))
  refs=[w.get('source'),*w.get('proof_sources',[]),*[c.get('source') for c in cs],*[s for c in cs for s in c.get('proof_sources',[])]]
  w['source_ids']=[s for s in dict.fromkeys(refs) if s in sources and s!='definitions']
  if not w.get('proof_summary'):w['proof_summary']=' '.join(dict.fromkeys(c['proof_summary'] for c in cs)) or 'The catalogue has not yet transcribed a proof summary; consult the definition-status note and source.'
  if not w.get('definition'):w['definition']='Full construction/promise definition has not yet been transcribed. Consult the cited source and exact locator.'
  w['scopes']=list({json.dumps(c['scope'],sort_keys=True):c['scope'] for c in cs}.values()) or ([w['scope']] if w.get('scope') else [])
  w['year']=sources[w['source']]['year'] if w.get('source') in sources else min((sources[s]['year'] for s in w['source_ids']),default=2026)
 checked_dates=[c.get('last_checked','') for c in d['claims']]
 return {'as_of':max([d.get('audit_date',''),*checked_dates]),'warning':notes['warning'],'summary':{'constructions':len(entries),'separation_claims_indexed':sum(c['kind']=='separation' and bool(mapping.get(c['id'])) for c in d['claims']),'no_polynomial_claims_indexed':sum(c['kind']=='no_polynomial_bound' and bool(mapping.get(c['id'])) for c in d['claims'])},'constructions':list(entries.values()),'claim_to_witness':{k:list(dict.fromkeys(v)) for k,v in mapping.items()}}
def main():
 d=json.loads((ROOT/'data/catalog.json').read_text());notes=json.loads((ROOT/'data/witness-constructions.json').read_text());out=build(d,notes);(ROOT/'data/separation-gallery.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print('Witness gallery:',out['summary'])
if __name__=='__main__':main()
