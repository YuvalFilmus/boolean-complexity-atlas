"""Independent rational moment/truncation checks and a native-coordinate example."""
from fractions import Fraction as F
from itertools import product
moments=0
for n in range(1,6):
 for coeff in product((-2,-1,0,1,2),repeat=n):
  vals=[sum(a*x for a,x in zip(coeff,s)) for s in product((-1,1),repeat=n)]
  m1=F(sum(abs(v) for v in vals),len(vals))
  m2=F(sum(v*v for v in vals),len(vals))
  m4=F(sum(v**4 for v in vals),len(vals))
  assert m2==sum(a*a for a in coeff)
  assert m4==3*m2*m2-2*sum(a**4 for a in coeff)
  assert 3*m1*m1>=m2
  moments+=1
truncations=0
for n in range(1,7):
 for w in product(range(1,5),repeat=n):
  weights=sorted(w,reverse=True);A=sum(weights)
  for m in range(1,n+1):
   tail=sum(a*a for a in weights[m:])
   assert 4*m*tail<=A*A
   truncations+=1
# x_a*(x_b+x_c) becomes z_b+z_c: native a-influence2,
# transformed prefix-coordinate z_a-influence0. Range preserved under free root.
values=[];nativeI=F(0)
for a,b,c in product((-1,1),repeat=3):
 z_a,z_b,z_c=a,a*b,a*c
 p=a*(b+c)
 assert p==z_b+z_c
 nativeI+=F((p-(-a)*(b+c))**2,4*8)
 values.append(p)
assert nativeI==2
qvals=[b+c for b,c in product((-1,1),repeat=2)]
freevals=[o*b+o*c for o,b,c in product((-1,1),repeat=3)]
assert (min(values),max(values))==(min(qvals),max(qvals))==(min(freevals),max(freevals))
print({'rational_Rademacher_moment_cases':moments,'exact_truncation_inequalities':truncations,'native_rootedge_influence':str(nativeI),'transformed_prefix_influence':0,'range':(min(values),max(values))})
