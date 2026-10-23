"""Exact independent checks of the fiber formula; no numerical tolerances."""
from itertools import permutations, product, combinations
from fractions import Fraction
from collections import defaultdict
import json
from math import factorial

def fall(a,t):
    ans=1
    for j in range(t): ans*=a-j
    return ans

def partitions(xs):
    if not xs:
        yield []
        return
    x, *rest = xs
    for blocks in partitions(rest):
        yield [(x,)] + blocks
        for j in range(len(blocks)):
            yield blocks[:j] + [(x,) + blocks[j]] + blocks[j+1:]

def check(lam,n,maxdegree):
    N=[a*n for a in lam]
    reps=list(product(*(list(permutations(range(z))) for z in N)))
    def proj(rep):
        return tuple(sorted(tuple(tuple(sorted(rep[i][b*a:(b+1)*a])) for i,a in enumerate(lam)) for b in range(n)))
    fibers=defaultdict(list)
    for rep in reps: fibers[proj(rep)].append(rep)
    edges=set(e for H in fibers for e in H)
    entries=[(i,p,v) for i,z in enumerate(N) for p in range(z) for v in range(z)]
    checked=0
    def formula(mon,H):
        pv={}; vv={}; V=defaultdict(lambda:[set() for _ in lam])
        for i,p,v in mon:
            if (i,p) in pv and pv[i,p]!=v: return Fraction(0)
            if (i,v) in vv and vv[i,v]!=p: return Fraction(0)
            pv[i,p]=v; vv[i,v]=p
            V[p//lam[i]][i].add(v)
        B=list(V); h=len(B)
        den=fall(n,h)
        for b in B:
            for i,a in enumerate(lam): den*=fall(a,len(V[b][i]))
        # Evaluating the polynomial restricts its potential edges to those in H.
        num=sum(all(all(V[b][i] <= set(e[i]) for i in range(len(lam))) for b,e in zip(B,es)) for es in permutations(H,h))
        # Independent partition-lattice expression; singleton J_U factors are 1.
        mobius_num=0
        for part in partitions(B):
            coeff=1
            nonconstant_factors=0
            for C in part:
                coeff*=(-1)**(len(C)-1)*factorial(len(C)-1)
                U=[set().union(*(V[b][i] for b in C)) for i in range(len(lam))]
                size=sum(map(len,U))
                if size>=2: nonconstant_factors+=1
                J=sum(all(U[i] <= set(e[i]) for i in range(len(lam))) for e in H)
                if size==1: assert J==1
                coeff*=J
            assert nonconstant_factors<=len(mon)//2
            mobius_num+=coeff
        assert mobius_num==num,(mon,H,mobius_num,num)
        return Fraction(num,den)
    for d in range(maxdegree+1):
        for mon in combinations(entries,d):
            for H,fr in fibers.items():
                exact=Fraction(sum(all(rep[i][p]==v for i,p,v in mon) for rep in fr),len(fr))
                predicted=formula(mon,H)
                assert exact==predicted,(lam,n,mon,H,exact,predicted)
                checked+=1
    return dict(lambda_vector=lam,n=n,maxdegree=maxdegree,representations=len(reps),hypermatchings=len(fibers),fiber_size=len(next(iter(fibers.values()))),exact_comparisons=checked)

if __name__=='__main__':
    results=[check((2,),2,3),check((1,1),2,3),check((2,1),2,3),check((2,),3,2)]
    print(json.dumps(results,indent=2))
