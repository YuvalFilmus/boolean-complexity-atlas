from itertools import product,combinations
from fractions import Fraction as F
from functools import lru_cache
N=4; xs=list(product((0,1),repeat=N))
adj={j:[j^(1<<(N-1-i)) for i in range(N)] for j in range(16)}
def matchings(left):
 if not left:yield ();return
 a=min(left)
 for b in adj[a]:
  if b in left:
   for rest in matchings(left-{a,b}):yield ((a,b),)+rest

def nullspace(A,n):
 A=[[F(v) for v in r] for r in A]; piv=[]; r=0
 for c in range(n):
  j=next((j for j in range(r,len(A)) if A[j][c]),None)
  if j is None:continue
  A[r],A[j]=A[j],A[r];z=A[r][c];A[r]=[v/z for v in A[r]]
  for j in range(len(A)):
   if j!=r and A[j][c]:
    z=A[j][c];A[j]=[u-z*v for u,v in zip(A[j],A[r])]
  piv.append(c);r+=1
 free=[c for c in range(n) if c not in piv]
 out=[]
 for c in free:
  v=[F(0)]*n;v[c]=1
  for j,p in enumerate(piv):v[p]=-A[j][c]
  out.append(v)
 return out

def depth(edges):
 masks=[(1<<a)|(1<<b) for a,b in edges]
 branches=[[sum(1<<j for j,x in enumerate(xs) if x[i]==b) for b in (0,1)] for i in range(N)]
 @lru_cache(None)
 def d(mask):
  if any(mask&~m==0 for m in masks):return 0
  return 1+min(max(d(mask&branches[i][b]) for b in (0,1)) for i in range(N) if all(mask&branches[i][b] for b in (0,1)))
 return d((1<<16)-1)

def constraints(edges,i):
 high=[s for s in range(16) if s.bit_count()>2]
 def chi(j,s):return (-1)**sum(xs[j][k] for k in range(N) if s>>(N-1-k)&1)
 # W_i: z_i times edge-constant function has Fourier degree <=2.
 return [[sum(chi(j,s^i) for j in edge) for edge in edges] for s in high]

ms=list(matchings(set(range(16))))
print('matchings',len(ms))
def irreducible(edges):
 partner={a:b for a,b in edges}|{b:a for a,b in edges}
 for pat in product((-1,0,1),repeat=4):
  if not 2<=pat.count(-1)<4:continue
  face={j for j,x in enumerate(xs) if all(b==-1 or x[i]==b for i,b in enumerate(pat))}
  if all(partner[j] in face for j in face):return False
 return True
print('irreducible_count',sum(irreducible(e) for e in ms))
for edges in ms:
 if not irreducible(edges):continue
 assert depth(edges)==4
 spaces=[nullspace(constraints(edges,i),8) for i in [0,1,2,4,8]]
 span=[v for sp in spaces for v in sp]
 rank=8-len(nullspace(span,8))
 print('edges',[(''.join(map(str,xs[a])),''.join(map(str,xs[b]))) for a,b in edges])
 print('dims',[len(sp) for sp in spaces],'totalspanrank',rank)

 break
# A rationally feasible last-query decomposition. Test whether the resulting
# degree-two Gram matrix is a nonadaptive two-query kernel.
pairs=[(0,4),(3,5),(1,6),(2,7)]
P=[[[F(0) for _ in range(8)] for _ in range(8)] for _ in range(5)]
for a,b in pairs:
 for j in (a,b):
  for k in (a,b):P[0][j][k]=F(1,2)
for qi,bit in enumerate((1,2,4,8),1):
 for a,b in pairs:
  if edges[a][0]^edges[a][1] == bit:continue
  for j in (a,b):
   for k in (a,b):P[qi][j][k]=F(1 if j==k else -1,6)
assert all(sum(P[q][j][k] for q in range(5))==(j==k) for j in range(8) for k in range(8))
for q,bit in enumerate((0,1,2,4,8)):
 A=constraints(edges,bit)
 assert all(sum(A[r][j]*P[q][j][k] for j in range(8))==0 for r in range(5) for k in range(8))
edgeof={v:j for j,e in enumerate(edges) for v in e}
def chi(v,s):return (-1)**((v&s).bit_count())
G=[[sum(F(chi(x,bit)*chi(y,bit))*P[q][edgeof[x]][edgeof[y]]
         for q,bit in enumerate((0,1,2,4,8))) for y in range(16)] for x in range(16)]
FG=[[sum(F(chi(x,a)*chi(y,b))*G[x][y] for x in range(16) for y in range(16))/256
     for b in range(16)] for a in range(16)]
off=[(a,b,FG[a][b]) for a in range(16) for b in range(16) if a!=b and FG[a][b]]
print('last-query POVM exact feasible; two-query Gram Fourier offdiagonals',len(off))
print('nonzero diagonal',[(a,FG[a][a]) for a in range(16) if FG[a][a]])

# All signed coordinate permutations preserving the selected matching.
from itertools import permutations
bits=(0,1,2,4,8)
edge_set={frozenset(e):i for i,e in enumerate(edges)}
autos=[]
for perm in permutations(range(4)):
 for flip in range(16):
  def act(x):
   y=flip
   for i in range(4):
    if x>>i&1:y^=1<<perm[i]
   return y
  image=[act(x) for x in range(16)]
  if not all(frozenset(image[x] for x in e) in edge_set for e in edges):continue
  ep=[edge_set[frozenset(image[x] for x in e)] for e in edges]
  qp=[0]+[bits.index(1<<perm[i]) for i in range(4)]
  autos.append((ep,qp))
print('matching_automorphisms',len(autos))

# Span of averaged, supported real symmetric block matrices. Complex Hermitian
# matrices can first be replaced by real parts, preserving all real constraints
# and positivity. No positivity is assumed in the affine calculation below.
symcoords=[(q,j,k) for q in range(5) for j in range(8) for k in range(j,8)]
avgbases=[]; echelon={}
for q,sp in enumerate(spaces):
 for a in range(len(sp)):
  for b in range(a,len(sp)):
   B=[[sp[a][j]*sp[b][k]+sp[b][j]*sp[a][k] for k in range(8)] for j in range(8)]
   A=[[[F(0) for k in range(8)] for j in range(8)] for qq in range(5)]
   for ep,qp in autos:
    for j in range(8):
     for k in range(8):A[qp[q]][ep[j]][ep[k]]+=B[j][k]
   flat=[A[qq][j][k] for qq,j,k in symcoords]
   v=flat[:]
   for pivot,w in sorted(echelon.items()):
    if v[pivot]:
     z=v[pivot];v=[x-z*y for x,y in zip(v,w)]
   pivot=next((j for j,x in enumerate(v) if x),None)
   if pivot is not None:
    z=v[pivot];echelon[pivot]=[x/z for x in v]
    avgbases.append(A)
print('invariant_supported_real_space_dimension',len(avgbases))

# Solving sum_q M_q=I in that invariant space. RREF augmented matrix.
A=[[sum(B[q][j][k] for q in range(5)) for B in avgbases]+[F(j==k)]
   for j in range(8) for k in range(j,8)]
def solve_affine(A,n):
 A=[r[:] for r in A];r=0;piv=[]
 for c in range(n):
  j=next((j for j in range(r,len(A)) if A[j][c]),None)
  if j is None:continue
  A[r],A[j]=A[j],A[r];z=A[r][c];A[r]=[v/z for v in A[r]]
  for j in range(len(A)):
   if j!=r and A[j][c]:
    z=A[j][c];A[j]=[u-z*v for u,v in zip(A[j],A[r])]
  piv.append(c);r+=1
 assert not any(all(not row[c] for c in range(n)) and row[n] for row in A)
 p=[F(0)]*n
 for j,c in enumerate(piv):p[c]=A[j][-1]
 kern=nullspace([row[:n] for row in A],n)
 return p,kern
sol,kern=solve_affine(A,len(avgbases))
print('normalized_invariant_affine_dimension',len(kern))
def combine(v):return [[[sum(v[t]*avgbases[t][q][j][k] for t in range(len(v))) for k in range(8)] for j in range(8)] for q in range(5)]
def fourier_gram(M):
 G=[[sum(F(chi(x,bit)*chi(y,bit))*M[q][edgeof[x]][edgeof[y]] for q,bit in enumerate(bits)) for y in range(16)] for x in range(16)]
 return [[sum(F(chi(x,a)*chi(y,b))*G[x][y] for x in range(16) for y in range(16))/256 for b in range(16)] for a in range(16)]
FGsol=fourier_gram(combine(sol))
quad=[a for a in range(16) if a.bit_count()==2]
assert all(FGsol[a][b]==FG[a][b] for a in quad for b in quad)
for v in kern:
 FGnull=fourier_gram(combine(v))
 scale=FGnull[quad[0]][quad[0]] / FG[quad[0]][quad[0]]
 assert all(FGnull[a][b]==scale*FG[a][b] for a in quad for b in quad)
print('all_invariant_normalized_quadratic_Grams_are_scalar_multiples',True)
print('quadratic_basis_order',quad)
print('16_times_base_quadratic_Gram',[[16*FG[a][b] for b in quad] for a in quad])
for bit in (1,2,4,8):
 star=[a for a in quad if a&bit]
 vals=[FG[a][b] for a,b in combinations(star,2)]
 assert all(abs(v)==F(1,16) for v in vals)
 assert vals[0]*vals[1]*vals[2]<0
print('frustrated_stars',4,'minimum_required_quadratic_trace',F(4*6,16),'available',sum(FG[a][a] for a in quad))
# Explicit two-parameter invariant family; this is easier to inspect than the
# arbitrary RREF basis. u=(1,...,1)/sqrt(8), and anti vectors use ordered pairs.
Ns=[
 [[0,1,-1,0],[1,0,-1,0],[-1,-1,0,0],[0,0,0,0]],
 [[0,0,1,-1],[0,0,0,0],[1,0,0,-1],[-1,0,-1,0]],
 [[0,-1,0,1],[-1,0,0,-1],[0,0,0,0],[1,-1,0,0]],
 [[0,0,0,0],[0,0,1,1],[0,1,0,1],[0,1,1,0]]]
tdir=[[[F(-4 if q==0 else 1,8) for k in range(8)] for j in range(8)] for q in range(5)]
edir=[[[F(0) for k in range(8)] for j in range(8)] for q in range(5)]
for q in range(1,5):
 for r,(a,b) in enumerate(pairs):
  for ss,(c,d) in enumerate(pairs):
   v=F(Ns[q-1][r][ss],2)
   edir[q][a][c]+=v;edir[q][b][d]+=v
   edir[q][a][d]-=v;edir[q][b][c]-=v
for D in (tdir,edir):
 assert all(sum(D[q][j][k] for q in range(5))==0 for j in range(8) for k in range(8))
 for q,bit in enumerate(bits):
  L=constraints(edges,bit)
  assert all(sum(L[r][j]*D[q][j][k] for j in range(8))==0 for r in range(5) for k in range(8))
 for ep,qp in autos:
  assert all(D[qp[q]][ep[j]][ep[k]]==D[q][j][k] for q in range(5) for j in range(8) for k in range(8))
assert any(tdir[0][j][k] for j in range(8) for k in range(8))
assert all(edir[0][j][k]==0 for j in range(8) for k in range(8))
assert any(edir[q][j][k] for q in range(1,5) for j in range(8) for k in range(8))
# Two independent invariant normalized homogeneous directions fill dim2.
Ft=fourier_gram(tdir);Fe=fourier_gram(edir)
assert all(Ft[a][b]==0 and Fe[a][b]==-FG[a][b] for a in quad for b in quad)
for N in Ns:
 inds=[i for i in range(4) if any(N[i])]
 assert len(inds)==3
 assert all(abs(N[i][j])==1 for i,j in combinations(inds,2))
 assert N[inds[0]][inds[1]]*N[inds[0]][inds[2]]*N[inds[1]][inds[2]]==1
print('explicit_family_complete',True,'quadratic_scalar','1-e', 'PSD_parameter_bounds','0<=t<=1/4; -1/6<=e<=1/3')
