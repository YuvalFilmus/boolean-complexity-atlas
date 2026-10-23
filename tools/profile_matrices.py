#!/usr/bin/env python3
"""Profile-specific exponent chains, retaining every symbolic prefactor and guard."""
from pathlib import Path
from fractions import Fraction
import json
ROOT=Path(__file__).resolve().parents[1]
def build(d,profiles):
 nodes=[m['id'] for m in d['measures'] if m['id'].startswith('domain') and m['id']!='domainCoverRadius'];out=[]
 for p in profiles['profiles']:
  paths={(a,a):(Fraction(1),'1',[],set()) for a in nodes}
  def edge(a,b,e,k,ids,guards=()):
   val=(Fraction(str(e)),k,ids,set(guards))
   if (a,b) not in paths or val[0]<paths[a,b][0]:paths[a,b]=val
  for c in d['claims']:
   if c['A'] not in nodes or c['B'] not in nodes or c['kind']!='upper_bound' or c.get('exponent') is None:continue
   if c['scope']['classes']==['composable_query_domain'] and c['id'].startswith(('domain-chain-','domain-added-')):
    edge(c['A'],c['B'],c['exponent'],'C['+c['id']+']',[c['id']])
  guards=['M>0'] if p['id'] in ['multislice','slice'] else []
  edge('domainD','domainBS',4,'K_D',['domain-parameterized-domainD-domainBS'],guards)
  edge('domainD','domainC',2,'K_P',['domain-parameterized-domainD-domainC'],guards)
  edge('domainC','domainBS',2,'K_C',['domain-parameterized-domainC-domainBS'])
  if p['id'] in ['product','permutation','perfect-matching','multislice','slice']:
   edge('domainDegree','domainS',2,'K_S',['profile-witnessing-degree-sensitivity'])
   edge('domainC','domainS',5,'K_T',['profile-certificate-sensitivity-five'])
  if p['id']=='hypermatching':edge('domainD','domainS',10,'K_G',['lambda-partite-D-sensitivity-product-lift'])
  if p['id']=='uniform-hypermatching':edge('domainD','domainS',10,'K_L',['uniform-hypermatching-D-sensitivity-lift'])
  if p['id'] in ['hypermatching','uniform-hypermatching']:
   edge('domainDegree','domainS',2,'K_H',['hypermatching-degree-sensitivity-descent'])
  if p['id']=='product':
   for b in ['domainC','domainUC']:edge('domainD',b,2,'1',['product-domainD-'+b+'-square'])
  for k in nodes:
   for a in nodes:
    for b in nodes:
     if (a,k) in paths and (k,b) in paths:
      u,v=paths[a,k],paths[k,b];e=u[0]*v[0]
      if (a,b) not in paths or e<paths[a,b][0]:
       coef=f'({u[1]})*({v[1]})^({u[0]})';paths[a,b]=(e,coef,u[2]+v[2],u[3]|v[3])
  rows=[]
  for a in nodes:
   for b in nodes:
    if a==b:continue
    row=dict(A=a,B=b,status='not_yet_indexed',globally_best_known_certified=False)
    if (a,b) in paths:
     v=paths[a,b];row.update(status='profile_parameter_upper_chain',exponent=str(v[0]),prefactor=v[1],claim_ids=v[2],assumptions=sorted(v[3]))
    rows.append(row)
  out.append(dict(profile=p['id'],domain=p['domain'],queries=p['queries'],parameter_bounds={k:p[k] for k in ['Delta','M','beta','beta_c','alpha']},coefficient_definitions=dict(K_D='beta^(-2)*max(Delta,n/M)',K_C='beta^(-1)',K_S='alpha^(-1)',K_P='max(Delta,n/M)',K_T='6*beta_c^(-1)*alpha^(-2)',K_L='10368*(2k-1)^10',K_G='10368*(2k-1)^10; k=|lambda|',K_H='(2k-1)^2; k=sum(lambda_i)',C='C[claimID] is the domain-independent constant under that claim’s error/query convention; not optimized here.'),source='DFLLV26',locator='Theorem 3.1 and Theorem 5.3; corresponding domain examples',cells=rows))
 return dict(warning='These are parameterized bounds for the listed query oracles, not uniform exponents after dropping parameters. K_D requires M>0. Full lambda-partite hypermatchings use a separate audited degree-descent bound and product-permutation query lift; no alpha-witnessing parameter for the hypermatching domain is asserted. Endpoint constants are not optimized.',profiles=out)
def main():
 out=build(json.loads((ROOT/'data/catalog.json').read_text()),json.loads((ROOT/'data/general-domains.json').read_text()));(ROOT/'data/profile-matrices.json').write_text(json.dumps(out,indent=2)+'\n');ls=['# Parameterized domain-profile comparisons','',out['warning'],'','K_D=beta^(-2)*max(Delta,n/M); K_C=beta^(-1); K_S=alpha^(-1); K_P=max(Delta,n/M); K_T=6*beta_c^(-1)*alpha^(-2). C[claimID] denotes the cited claim’s domain-independent constant. Composition multiplies constants and raises them to the preceding exponent.','']
 for p in out['profiles']:
  count=sum(c['status']!='not_yet_indexed' for c in p['cells']);ls+=['## '+p['profile'],'',p['domain']+'; '+p['queries'], '',str(count)+'/132 upper chains.','', '| A | B | Exponent | Required guards |','|---|---|---:|---|']
  for c in p['cells']:ls.append('| '+c['A']+' | '+c['B']+' | '+c.get('exponent','—')+' | '+', '.join(c.get('assumptions',[]))+' |')
 ls+=['','Full symbolic prefactors, claim IDs and domain parameter bounds are retained in data/profile-matrices.json.']
 (ROOT/'docs/profile-matrices.md').write_text('\n'.join(ls)+'\n');print({p['profile']:sum(c['status']!='not_yet_indexed' for c in p['cells']) for p in out['profiles']})
if __name__=='__main__':main()
