"""Exact structural checks for the cube-first sensitivity refinement."""
from itertools import product, combinations

def partial_matchings(vertices):
    if not vertices:
        yield (); return
    a,*rest=vertices
    yield from partial_matchings(rest)
    for j,b in enumerate(rest):
        for tail in partial_matchings(rest[:j]+rest[j+1:]):yield ((a,b),)+tail

def subsets(xs):
    for m in range(1,len(xs)+1):yield from combinations(xs,m)

faces=0;loop_checks=0;native_neighbors=0;families=0
for lam,n in [((2,),2),((2,),3),((2,),4),((3,),3),((3,),2),((4,),2),((1,1),2),((1,1),3),((1,1),4),((2,1),2),((1,1,1),2)]:
    offset=0;colors=[];groups=[]
    for l in lam:
        colors.append(tuple(range(offset,offset+l*n)))
        groups.extend(g for g in range(n) for _ in range(l));offset+=l*n
    def project(p):
        return frozenset(frozenset(p[a] for a,g in enumerate(groups) if g==b) for b in range(n))
    for local in product(*(tuple(partial_matchings(list(c))) for c in colors)):
        axes=sum(local,());D=len(axes)
        if not D:continue
        states=[]
        for mask in range(1<<D):
            p=list(range(offset))
            for i,(a,b) in enumerate(axes):
                if mask>>i&1:p[a],p[b]=p[b],p[a]
            states.append(project(p))
        for i,(a,b) in enumerate(axes):
            if groups[a]==groups[b]:
                for mask in range(1<<D):
                    assert states[mask]==states[mask^(1<<i)]
                    loop_checks+=1
        if any(groups[a]==groups[b] for a,b in axes):continue
        families+=1
        for selected in subsets(tuple(range(D))):
            touched=[groups[v] for i in selected for v in axes[i]]
            if len(set(touched))<len(touched):continue
            other=tuple(i for i in range(D) if i not in selected)
            for fixed in range(1<<len(other)):
                base=sum(((fixed>>j)&1)<<i for j,i in enumerate(other))
                masks=[base+sum(((bits>>j)&1)<<i for j,i in enumerate(selected)) for bits in range(1<<len(selected))]
                assert len({states[m] for m in masks})==len(masks)
                for mask in masks:
                    removed=[states[mask]-states[mask^(1<<i)] for i in selected]
                    assert all(len(r)==2 for r in removed)
                    assert sum(map(len,removed))==len(set().union(*removed))
                    native_neighbors+=len(selected)
                faces+=1
print({'families':families,'fixed_matching_faces':faces,'loop_dummy_axis_checks':loop_checks,'native_neighbor_checks':native_neighbors,'cases':11})
