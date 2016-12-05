# -*- coding: utf-8 -*-

from topol import order
from collections import defaultdict


def longest2(n, edges):
    ordered = order(n, edges)
    incoming = defaultdict(list)
    back = defaultdict(lambda: (0, -1))
    for a, b in edges:
        incoming[b].append(a)

    for node in ordered:
        if len(incoming[node]) > 0:
            back[node] = max([(back[pre_node][0] + 1, pre_node) for pre_node in incoming[node]])

    return back_trace(back)

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

    return back_trace(back)


def back_trace(back):
    res = []
    curr = max(back, key=back.get)
    length = back[curr][0]
    while curr > -1:
        res.append(curr)
        _, pre = back[curr]
        curr = pre
    return length, list(reversed(res))


if __name__ == '__main__':
    print longest(9, [(0,2), (1,2), (2,5), (2,3), (2,4), (3,4), (4,6), (4,5), (5,6), (6,7), (6,8)])
    print longest(9, [(0,2), (1,2), (2,5), (2,3), (3,4), (4,6), (4,5), (5,6), (6,7), (6,8)])
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,5),(3,4),  (4,5), (5,6), (5,7)])
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,7), (5,6)])
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
    print longest(8, [(6,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,0), (5,7)])
    print longest(8, [(3,2), (1,2), (2,0), (2,4), (0,4), (0,5), (5,6), (5,7)])
    print longest(5, [(2,1), (1,3), (3,4), (2,3), (4, 0), (1, 0)])
