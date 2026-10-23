"""Exact finite checks for research-other-round2.md; no numerical optimizer."""
from itertools import combinations, product
from functools import lru_cache

tables = 0
for a,b,c,d in product(range(6), repeat=4):
    if a+d != b+c:
        continue
    u = [min(a,b), min(c,d)]
    v = [a-u[0], b-u[0]]
    assert min(*u,*v) >= 0
    assert c-u[1] == v[0] and d-u[1] == v[1]
    tables += 1

n=3
xs=list(product((0,1),repeat=n))
certs=[tuple(zip(ij,v)) for ij in combinations(range(n),2) for v in product((0,1),repeat=2)]
cmasks=[sum(1<<j for j,x in enumerate(xs) if all(x[i]==b for i,b in c)) for c in certs]
branches=[[sum(1<<j for j,x in enumerate(xs) if x[i]==b) for b in (0,1)] for i in range(n)]

def depth(inds):
    @lru_cache(None)
    def d(mask):
        if any(mask & ~cmasks[j] == 0 for j in inds):
            return 0
        return 1+min(max(d(mask & branches[i][b]) for b in (0,1))
                     for i in range(n) if all(mask & branches[i][b] for b in (0,1)))
    return d(255)

def star_criterion(inds):
    support={certs[j] for j in inds}
    # Positive row/column components in a nonnegative additive pair table
    # require a full pair of certificates sharing a root literal.
    def star(i,b):
        return any(all(tuple(sorted(((i,b),(j,t)))) in support for t in (0,1))
                   for j in range(n) if j != i)
    return any(star(i,0) and star(i,1) for i in range(n))

counts={2:0,3:0}
for bits in range(1<<len(certs)):
    inds=tuple(j for j in range(len(certs)) if bits>>j&1)
    union=0
    for j in inds:
        union |= cmasks[j]
    if union != 255:
        continue
    d=depth(inds)
    assert d in (2,3)
    assert star_criterion(inds) == (d<=2)
    counts[d]+=1

example=[((0,0),(1,0)),((0,0),(1,1)),((0,1),(1,0)),((0,1),(2,0)),((1,1),(2,1))]
assert depth(tuple(certs.index(c) for c in example))==3
print({'additive_integer_tables_checked':tables,'all_three_bit_supports_checked':4096,
       'total_covers_by_D':counts,'explicit_example_D':3})

# Extend independent depth recurrence to mixed singleton/pair covers. Opposite
# singleton pairs are omitted because they have a one-query solver immediately.
allcerts=certs+[ ((i,b),) for i in range(n) for b in (0,1)]
allmasks=cmasks+[sum(1<<j for j,x in enumerate(xs) if x[i]==b) for i in range(n) for b in (0,1)]
def mixed_depth(inds):
    @lru_cache(None)
    def d(mask):
        if any(mask & ~allmasks[j]==0 for j in inds):
            return 0
        return 1+min(max(d(mask&branches[i][b]) for b in (0,1))
                     for i in range(n) if all(mask&branches[i][b] for b in (0,1)))
    return d(255)

def residual_criterion(inds,fixed):
    residual=[]
    for j in inds:
        if j>=12:
            continue
        c=allcerts[j]
        if any(i in fixed and fixed[i]!=b for i,b in c):
            continue
        r=tuple((i,b) for i,b in c if i not in fixed)
        if not r:
            return True
        residual.append(r)
    support=set(residual)
    free=[i for i in range(n) if i not in fixed]
    def branch(i,b):
        return ((i,b),) in support or any(
            all(tuple(sorted(((i,b),(j,t)))) in support for t in (0,1))
            for j in free if j!=i)
    return any(branch(i,0) and branch(i,1) for i in free)

mixed_counts={1:0,2:0,3:0}
for singleton_policy in product((-1,0,1),repeat=n):
    fixed={i:1-b for i,b in enumerate(singleton_policy) if b!=-1}
    singleton_inds=tuple(12+2*i+b for i,b in enumerate(singleton_policy) if b!=-1)
    for bits in range(4096):
        inds=tuple(j for j in range(12) if bits>>j&1)+singleton_inds
        union=0
        for j in inds:
            union |= allmasks[j]
        if union != 255:
            continue
        d=mixed_depth(inds)
        assert residual_criterion(inds,fixed)==(d<=2), (inds,d,fixed)
        mixed_counts[d]+=1
print({'mixed_singleton_pair_supports_checked':27*4096,
       'mixed_total_covers_by_D':mixed_counts})
