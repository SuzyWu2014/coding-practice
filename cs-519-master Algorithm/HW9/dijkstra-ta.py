__author__ = "liang huang"

from heapdict import heapdict
from collections import defaultdict

def shortest(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges:
        edges[u].append((v, cost))
        edges[v].append((u, cost))
    h = heapdict()
    h[0] = 0 # alternatively, you can also set everything else to +inf
    back = {}
    popped = set() # those already popped (i.e., black nodes)
    while len(h) > 0:
        v, d = h.popitem()
        popped.add(v)
        if v == n-1: # target is popped (fixed)
            return d, solution(v, back)
        for (u, cost) in edges[v]:
            if u not in popped: # N.B.: important check
                newd = d + cost
                if u not in h or newd < h[u]: # forward update;
                    h[u] = newd # automatic decrease-key()
                    back[u] = v
    return None # target is not reachable

def solution(v, back):
    if v == 0:
        return [0]
    return solution(back[v], back) + [v]

print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
print shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]) # unreachable
