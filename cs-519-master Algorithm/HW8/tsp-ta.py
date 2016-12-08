''' graph input:
a pair: the number of nodes n, and the list of edges.
(n, [(u, v, cost), ... ])

internal graph representation: adjacency list (hash: node->list_of_neighbors)
'''
from collections import defaultdict

def bottom_up(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges: # undirected
        edges[u].append((v, cost))
        edges[v].append((u, cost))

    best = defaultdict(lambda : defaultdict(lambda: float("inf")))
    # best[size][S, i]  --- organize best by size (|S|)
    best[1][1, 0] = 0 # {0}

    back = {} # back[S, i], no need to organize by size

    for size in xrange(2, n+1): # 2 to n
        for S, j in best[size-1]: # all reachable (S, j) with |S|=size-1
            for i, cost in edges[j]:
                if not ((1<<i) & S):
                    newS = S | (1 << i)  # expand visited set
                    newcost = best[size-1][S, j] + cost
                    if newcost < best[size][newS, i]: # forward update
                        best[size][newS, i] = newcost
                        back[newS, i] = j, S

    full = 2**n - 1 # 11..1
    # only works for undirected graph
    goal, goalj = min((best[n][full, j] + cost, j) for j, cost in edges[0])

    if goal < float("inf"):
        return goal, solution(back, full, goalj) + [0]
    return None

def solution(back, S, v):
    if v == 0:
        return [0]
    j, S1 = back[S, v]
    return solution(back, S1, j) + [v]

print bottom_up(3, [(0,1,1), (1,2,2), (2,0,3)])
print bottom_up(3, [(0,1,1), (1,2,2)]) # impossible
print bottom_up(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,1), (1,3,6)])
print bottom_up(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,1), (1,3,6), (3,0,1)])
