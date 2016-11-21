# -*- coding: utf-8 -*-

from topol import order
from collections import defaultdict

def longest(n, edges):
    """
    given a DAG (guaranteed acyclic!), output a pair (l, p)

    where l is the length of the longest path (number of edges),
        and p is the path.
    """
    ordered = order(n, edges)
    outgoing = defaultdict(list)
    back = defaultdict(lambda: (0, -1))
    for a, b in edges:
        outgoing[a].append(b)

    for node in ordered:
        for next_node in outgoing[node]:
            back[next_node] = (back[node][0] + 1, node)
    print back
    return back[max(back, key=back.get)][0], back_trace(back)



def back_trace(back):
    res = []
    curr = max(back, key=back.get)
    while curr > -1:
        res.append(curr)
        _, pre = back[curr]
        curr = pre
    return list(reversed(res))

if __name__ == '__main__':
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
