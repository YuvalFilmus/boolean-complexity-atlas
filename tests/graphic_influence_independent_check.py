"""Independent structural checker; no imports from the author verifier.
Exhaustive endpoint-load dynamic programming replaces network flow.
All substantive checks use integers. This checks finite cases, not the universal proof.
"""
import itertools as it, json, random
from pathlib import Path

def rank(xs):
    piv={}
    for x in xs:
        while x:
            k=x.bit_length()-1
            if k in piv: x^=piv[k]
            else: piv[k]=x; break
    return len(piv)

def energy_check(labels, edges, energies, n, allocation=True):
    cuts=[sum(b for (u,v),b in zip(edges,energies) if ((labels[u]^labels[v])>>i)&1) for i in range(n)]
    t=max(cuts,default=0); V=sum(energies); m=len(labels)
    for mask in range(1,1<<m):
        internal=sum(b for (u,v),b in zip(edges,energies) if (mask>>u)&1 and (mask>>v)&1)
        assert internal<=t*(mask.bit_count()-1)
    if allocation:
        # Enumerate possible integral endpoint loads, rather than run any flow.
        loads={(0,)*m}
        for (u,v),b in zip(edges,energies):
            nxt=set()
            for old in loads:
                for k in range(b+1):
                    new=list(old); new[u]+=k; new[v]+=b-k
                    if new[u]<=t and new[v]<=t: nxt.add(tuple(new))
            loads=nxt
            assert loads
        assert all(sum(z)==V and max(z,default=0)<=t for z in loads)
    return t,V

n=3; pairs=list(it.combinations(range(4),2)); polynomial_cases=0
basis_list=[b for b in it.permutations(range(1,8),3) if rank(b)==3]
for basis in basis_list:
    labels=(0,)+basis
    support=[labels[u]^labels[v] for u,v in pairs]
    assert len(set(support))==6 and 0 not in support
    for a in it.product((-1,0,1),repeat=6):
        if not any(a): continue
        b=[z*z for z in a]
        t,V=energy_check(labels,pairs,b,n,allocation=False)
        native=[sum(aa*aa for S,aa in zip(support,a) if (S>>i)&1) for i in range(n)]
        assert max(native)==t
        nativevalues=[sum(aa*(-1 if (S&x).bit_count()%2 else 1) for S,aa in zip(support,a)) for x in range(8)]
        freevalues=[]
        anchored=[]
        for z in it.product((-1,1),repeat=4):
            q=sum(aa*z[u]*z[v] for (u,v),aa in zip(pairs,a))
            freevalues.append(q)
            if z[0]==1: anchored.append(q)
        assert sorted(nativevalues)==sorted(anchored)
        assert min(freevalues)==min(nativevalues) and max(freevalues)==max(nativevalues)
        W=max(nativevalues)-min(nativevalues)
        assert V>0 and W>0 and V*V<=8*t*W*W<=12*t*W*W
        polynomial_cases+=1

cut_cases=0
# Labels may now be dependent, with no anchor/basis requirement.
for labels in it.combinations(range(8),4):
    for energies in it.product((0,1),repeat=6):
        energy_check(labels,pairs,energies,3)
        cut_cases+=1
rng=random.Random(5302026)
for _ in range(500):
    labels=tuple(rng.sample(range(16),5))
    edges=list(it.combinations(range(5),2))
    energies=tuple(rng.randrange(4) for e in edges)
    energy_check(labels,edges,energies,4)
    cut_cases+=1
# Constant/empty graph cases, including N=0 and no vertices.
for labels in [(),(0,)]: energy_check(labels,[],[],0)
# Explicit dependent-character trap: all seven nonzero supports on 3 bits.
# p=8*1[x=0]-1 has original range8, free independent star range14.
labels=list(range(8)); original=[sum((-1 if (s&x).bit_count()%2 else 1) for s in range(1,8)) for x in range(8)]
assert max(original)-min(original)==8 and 2*(len(labels)-1)==14
out={'invertible_bases_exhausted':len(basis_list),'signed_polynomials_exhausted':polynomial_cases,
     'distinct_label_weighted_cut_cases':cut_cases,'allocation_method':'exhaustive endpoint-load DP; no max-flow',
     'checked_constants':[12,8], 'dependent_label_range_counterexample':{'native_oscillation':8,'free_graph_oscillation':14},'status':'PASS'}
if __name__=='__main__':Path(__file__).with_name('graphic-influence-fresh-checks-round5.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
