# -*- coding: utf-8 -*-

from topol import order
from collections import defaultdict


def longest2(n, edges):
    res = []
    incoming = defaultdict(int)
    outgoing = defaultdict(list)
    visited = set()

    for a, b in edges:
        incoming[b] += 1
        outgoing[a].append(b)

    curr = deque([node for node in xrange(n) if incoming[node] == 0])

    while curr:
        node = curr.popleft()
        res.append(node)
        for next_node in outgoing[node]:
            incoming[next_node] -= 1
            visited.add((node, next_node))
            if incoming[next_node] == 0:
                curr.append(next_node)

    return None if len(edges) != len(visited) else res

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
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,7), (5,6)])
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
    print longest(8, [(6,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,0), (5,7)])
    print longest(8, [(3,2), (1,2), (2,0), (2,4), (0,4), (0,5), (5,6), (5,7)])
    print longest(5, [(2,1), (1,3), (3,4), (2,3), (4, 0), (1, 0)])
