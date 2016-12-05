from collections import defaultdict

def order(n, edges):
    print edges
    degrees = defaultdict(lambda : 1) # dummy source -> all v
    for u in edges:
        print "u", u
        for v in edges[u]:
            print v
            degrees[v] += 1
    edges[-1] = range(n) # dummy source -> everybody

    current = [-1] # zero-degrees nodes
    front = 0  # queue head pointer
    out = [] # final output order
    while front < len(current):
        v = current[front]
        out.append(v)
        front += 1 # pop queue head
        for u in edges[v]:
            degrees[u] -= 1
            if degrees[u] == 0:
                current.append(u)
    if len(out) == n+1:
        return out[1:] # excluding dummy source
    return None # cycle found

def longest(n, _edges):

    def solution(v):
        if v not in back: # doesn't need to start with 0
            return [v]
        return solution(back[v]) + [v]

    edges = defaultdict(list)
    for (u,v) in _edges:
        edges[u].append(v)
    topol = order(n, edges)
    for u in edges:
        edges[u].append(-1) # dummy sink (all v -> sink)
    best = defaultdict(int)
    back = {}
    for u in topol:
        for v in edges[u]: # forward update
            if best[u] + 1 > best[v]:
                best[v] = best[u] + 1
                back[v] = u
    return best[-1]-1, solution(back[-1])

print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
