"""Fresh exact verification of a published-candidate finite certificate.
No imports from earlier author/reviewer checkers; direct input-pair Fourier sums.
"""
from itertools import permutations,product,combinations
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
E=((0,8),(1,5),(2,3),(4,6),(7,15),(9,11),(10,14),(12,13));Q=(0,1,2,4,8)
eof={x:j for j,e in enumerate(E) for x in e};assert len(eof)==16
assert all((a^b).bit_count()==1 for a,b in E)
def sign(a,x):return 1-2*((a&x).bit_count()%2)
# Recompute full signed coordinate automorphism group from its definition.
autos=[]
for p in permutations((0,1,2,3)):
 for t in range(16):
  xs=[t^sum(((x>>i)&1)<<p[i] for i in range(4)) for x in range(16)]
  if all(eof[xs[a]]==eof[xs[b]] for a,b in E):
   autos.append(([eof[xs[a]] for a,b in E],{0:0,**{1<<i:1<<p[i] for i in range(4)}}))
assert len(autos)==48
coords={(q,a,b) for q in Q for a in range(8) for b in range(a,8)}
reps=((0,0,1),(0,0,0),(0,0,4),(1,0,0),(1,0,1),(1,0,2),(1,0,3),(1,0,4),(1,2,2),(1,2,7))
where={}
for j,(q,a,b) in enumerate(reps):
 orb={(qs[q],min(es[a],es[b]),max(es[a],es[b])) for es,qs in autos}
 assert not set(where).intersection(orb)
 where.update({c:j for c in orb})
assert set(where)==coords
def coord(q,a,b):return where[(q,min(a,b),max(a,b))]
# Build all linear constraints on 10 orbit unknowns, including redundant ones.
rows=[]
for q in Q:
 for s in range(16):
  if s.bit_count()<=2:continue
  for b in range(8):
   row=[F(0)]*11
   for a in range(8):row[coord(q,a,b)]+=sum(sign(s^q,x) for x in E[a])
   rows.append(row)
for a in range(8):
 for b in range(8):
  row=[F(0)]*11
  for q in Q:row[coord(q,a,b)]+=1
  row[-1]=int(a==b);rows.append(row)
# Affine rank and consistency, without accepting the prior claimed dimensions.
red=[r[:] for r in rows];rank=0
for j in range(10):
 k=next((k for k in range(rank,len(red)) if red[k][j]),None)
 if k is None:continue
 red[rank],red[k]=red[k],red[rank];v=red[rank][j];red[rank]=[x/v for x in red[rank]]
 for k in range(len(red)):
  if k!=rank and red[k][j]:
   v=red[k][j];red[k]=[a-v*b for a,b in zip(red[k],red[rank])]
 rank+=1
assert rank==8 and not any(not any(r[:10]) and r[10] for r in red)
b=[F(x) for x in (0,F(1,2),F(1,2),F(1,6),0,0,0,F(-1,6),0,0)]
v=[F(x) for x in (0,0,0,0,-1,0,1,0,0,0)]
w=[F(x) for x in (-4,-4,-4,1,2,1,0,1,1,1)]
assert any(v[j]*w[k]!=v[k]*w[j] for j in range(10) for k in range(10))
for r in rows:
 assert sum(r[j]*b[j] for j in range(10))==r[10]
 assert sum(r[j]*v[j] for j in range(10))==0
 assert sum(r[j]*w[j] for j in range(10))==0
quad=(3,5,6,9,10,12)
B=((2,1,1,1,-1,0),(1,2,1,-1,0,1),(1,1,2,0,1,-1),(1,-1,0,2,-1,-1),(-1,0,1,-1,2,-1),(0,1,-1,-1,-1,2))
scales=[]
for values in (b,v,w):
 G=[[sum(sign(q,x)*sign(q,y)*values[coord(q,eof[x],eof[y])] for q in Q) for y in range(16)] for x in range(16)]
 H=[[sum(sign(s,x)*G[x][y]*sign(t,y) for x in range(16) for y in range(16))/256 for t in quad] for s in quad]
 scale=8*H[0][0];assert all(H[i][j]==scale*F(B[i][j],16) for i in range(6) for j in range(6))
 scales.append(scale)
assert scales==[1,-2,2]
for bit in (1,2,4,8):
 inds=[i for i,s in enumerate(quad) if s&bit]
 vals=[B[i][j] for i,j in combinations(inds,2)]
 assert len(inds)==3 and all(abs(x)==1 for x in vals) and vals[0]*vals[1]*vals[2]==-1
for i,j in combinations(range(6),2):
 assert sum(bool(quad[i]&bit and quad[j]&bit) for bit in (1,2,4,8))==(quad[i]&quad[j]).bit_count()
 assert (B[i][j]==0)==(quad[i]&quad[j]==0)
assert sum(B[i][i] for i in range(6))==12
# Directly identify the known KRS 4-MAJ partition: first four outputs value0.
for x in range(16):
 bits=[(x>>(3-i))&1 for i in range(4)];weight=sum(bits)
 val=int(weight>2 or (weight==2 and bits[0]))
 assert val==int(eof[x]>=4)
result={'status':'fresh rational finite certificate verified','automorphisms':len(autos),'orbit_unknowns':len(reps),'constraint_rank':rank,'affine_dimension':10-rank,'quadratic_scales':[str(s) for s in scales],'trace_required_per_positive_scale':'3/2','trace_available':'3/4','matching_is_exact_KRS_4MAJ_partition':True,'method':'direct input-pair Fourier transform; exact Fraction arithmetic; no prior-checker imports'}
if __name__=='__main__':Path(__file__).with_name('width-three-fresh-check-round4.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
