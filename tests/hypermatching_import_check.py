"""Exact finite checks of the repaired imported permutation witnesses."""
from itertools import permutations, combinations, product
from math import factorial

def parts(n, bound=None):
    if not n:
        yield (); return
    for a in range(min(n,n if bound is None else bound),0,-1):
        for p in parts(n-a,a):yield (a,)+p

def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def rows(shape):
    a=0;out=[]
    for x in shape:out.append(tuple(range(a,a+x)));a+=x
    return out

def char_vector(shape):
    n=sum(shape); rs=rows(shape)
    cs=[tuple(r[j] for r in rs if j<len(r)) for j in range(shape[0])]
    summands=[]
    for qs in product(*(list(permutations(c)) for c in cs)):
        s=1;mp={}
        for c,q in zip(cs,qs):
            s*=sign(tuple(c.index(v) for v in q));mp.update(zip(c,q))
        summands.append((s,tuple(frozenset(mp[v] for v in r) for r in rs)))
    ps=list(permutations(range(n)))
    def val(p):
        rr=tuple(frozenset(p[v] for v in r) for r in rs)
        return sum(s for s,b in summands if rr==b)
    return ps,[val(p) for p in ps],cs

covariance_checks=0;orthogonality_checks=0
for n in range(2,6):
    for shape in parts(n):
        ps,chi,cs=char_vector(shape);lookup=dict(zip(ps,chi));d=n-shape[0]
        assert all(v in (-1,0,1) for v in chi)
        assert any(chi)
        for c in cs:
            for b,z in combinations(c,2):
                for p,v in zip(ps,chi):
                    q=tuple(z if x==b else b if x==z else x for x in p)
                    assert lookup[q]==-v
                    covariance_checks+=1
        # Canonical B and A, all consistent partial bijection monomials below depth.
        for e in range(d):
            for aa in combinations(range(n),e):
                for bb in permutations(range(n),e):
                    dot=sum(v for p,v in zip(ps,chi) if all(p[a]==b for a,b in zip(aa,bb)))
                    assert dot==0,(n,shape,aa,bb,dot)
                    orthogonality_checks+=1
p=(1,0,2) # one-based (2,1,3)
chi=lambda p:int(p[2]==2)-int(p[2]==0)
right=(p[2],p[1],p[0]);left=tuple(2 if x==0 else 0 if x==2 else x for x in p)
assert (chi(p),chi(right),chi(left))==(1,0,-1)
print({'orientation_counterexample': [1,0,-1], 'output_covariance_checks':covariance_checks,'lower_filtration_orthogonality_checks':orthogonality_checks,'max_n':5})
