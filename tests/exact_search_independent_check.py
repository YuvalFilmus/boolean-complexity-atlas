"""Independent exact support audit via cube matchings, not row decomposition."""
from itertools import combinations,product
from functools import lru_cache

inputs=tuple(product((0,1),repeat=3))
certificates=tuple(tuple(zip(coords,bits)) for coords in combinations(range(3),2) for bits in product((0,1),repeat=2))
valid=tuple(frozenset(i for i,x in enumerate(inputs) if all(x[j]==b for j,b in c)) for c in certificates)
assert all(len(v)==2 for v in valid)
even=tuple(i for i,x in enumerate(inputs) if sum(x)%2==0)
odd=tuple(i for i,x in enumerate(inputs) if sum(x)%2)

@lru_cache(None)
def depth(support,remaining):
    state=frozenset(remaining)
    if any(state <= valid[c] for c in support):return 0
    ans=99
    for j in range(3):
        children=[tuple(i for i in remaining if inputs[i][j]==b) for b in (0,1)]
        if all(children):ans=min(ans,1+max(depth(support,c) for c in children))
    return ans

def perfect_matching(support):
    # A nonnegative normalized codim2 partition is a fractional perfect matching
    # of this bipartite cube subgraph. Hall's criterion is necessary/sufficient.
    adjacency={i:set() for i in even}
    for c in support:
        a,b=tuple(valid[c])
        if a not in adjacency:a,b=b,a
        adjacency[a].add(b)
    for size in range(1,5):
        for subset in combinations(even,size):
            if len(set().union(*(adjacency[i] for i in subset)))<size:return False
    return True

counts={2:0,3:0};hall_feasible=0
for mask in range(1<<12):
    support=tuple(c for c in range(12) if mask>>c&1)
    is_total=set().union(*(valid[c] for c in support))==set(range(8))
    feasible=perfect_matching(support)
    if not is_total:
        assert not feasible;continue
    d=depth(support,tuple(range(8)))
    assert d in counts
    counts[d]+=1
    assert feasible==(d<=2),(support,d,feasible)
    hall_feasible+=feasible
example=(((0,0),(1,0)),((0,0),(1,1)),((0,1),(1,0)),((0,1),(2,0)),((1,1),(2,1)))
ix=tuple(certificates.index(c) for c in example)
assert depth(ix,tuple(range(8)))==3 and not perfect_matching(ix)
print({'supports':4096,'total_by_D':counts,'normalized_fractional_partitions_feasible':hall_feasible,'explicit_obstruction_D':3})
