"""Exact finite checks of graphic character support and native cut energy lemma."""
from itertools import combinations
from collections import deque
from fractions import Fraction as F
import random,json
from pathlib import Path
rng=random.Random(2026102304)
def rank(rows):
 piv={}
 for v in rows:
  while v:
   j=v.bit_length()-1
   if j not in piv:piv[j]=v;break
   v^=piv[j]
 return len(piv)

def endpoint_flow(energies,nv,t):
 # Source->edge supplies, edge->endpoint capacity V, endpoint->sink t.
 V=sum(b for a,c,b in energies);src=0;edge0=1;vert0=1+len(energies);sink=vert0+nv
 cap={};nbr={i:set() for i in range(sink+1)}
 def add(a,b,c):
  cap[a,b]=cap.get((a,b),F(0))+c;cap.setdefault((b,a),F(0));nbr[a].add(b);nbr[b].add(a)
 for i,(a,b,w) in enumerate(energies):
  add(src,edge0+i,F(w));add(edge0+i,vert0+a,F(V));add(edge0+i,vert0+b,F(V))
 for a in range(nv):add(vert0+a,sink,F(t))
 residual=cap.copy();sent=F(0)
 while True:
  path={src:None};queue=deque([src])
  while queue and sink not in path:
   a=queue.popleft()
   for b in nbr[a]:
    if b not in path and residual[a,b]>0:path[b]=a;queue.append(b)
  if sink not in path:break
  a=sink;delta=F(V)
  while path[a] is not None:delta=min(delta,residual[path[a],a]);a=path[a]
  a=sink
  while path[a] is not None:
   b=path[a];residual[b,a]-=delta;residual[a,b]+=delta;a=b
  sent+=delta
 assert sent==V
 loads=[cap[vert0+a,sink]-residual[vert0+a,sink] for a in range(nv)]
 assert sum(loads)==V and all(0<=w<=t for w in loads)
 assert all(w<=sum(b for u,v,b in energies if a in (u,v)) for a,w in enumerate(loads))
 return loads
cases=0;induced_checks=0;best_ratio=None
for n in range(1,8):
 for rep in range(45):
  while True:
   basis=rng.sample(range(1,1<<n),n)
   if rank(basis)==n:break
  vertexlabels=[0]+basis;nv=n+1
  pairs=list(combinations(range(nv),2));chosen=[e for e in pairs if rng.random()<.45]
  if not chosen:chosen=[rng.choice(pairs)]
  weighted=[(a,b,rng.choice((-1,1))*rng.randint(1,5)) for a,b in chosen]
  terms=[(vertexlabels[a]^vertexlabels[b],w) for a,b,w in weighted]
  assert len(set(s for s,w in terms))==len(terms)
  influence=[sum(w*w for s,w in terms if s>>i&1) for i in range(n)]
  t=max(influence);V=sum(w*w for s,w in terms)
  vals=[sum(w*(-1 if (s&x).bit_count()%2 else 1) for s,w in terms) for x in range(1<<n)]
  W=max(vals)-min(vals);assert W>0
  assert 12*t*W*W>=V*V
  energies=[(a,b,w*w) for a,b,w in weighted]
  for U in range(1,1<<nv):
   internal=sum(w for a,b,w in energies if U>>a&1 and U>>b&1)
   assert internal<=t*(U.bit_count()-1)
   induced_checks+=1
  endpoint_flow(energies,nv,t)
  ratio=F(t*W*W,V*V);best_ratio=ratio if best_ratio is None else min(best_ratio,ratio)
  cases+=1
result={'graphic_basis_cases':cases,'induced_density_checks':induced_checks,'exact_endpoint_flows':cases,'all_influence_inequalities_passed':True,'minimum_observed_Imax_W2_over_V2':str(best_ratio),'limitations':'finite exact checks; not universal proof or novelty certification'}
if __name__=='__main__':Path(__file__).with_name('aa-graphic-cuts-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
