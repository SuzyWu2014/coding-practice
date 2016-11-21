from collections import defaultdict, namedtuple
from heapdict import heapdict


def shortest_native(n, edges):
    """
    Given an undirected graph, find the shortest path from source (node 0)
    to target (node n-1).
    """
    distances = defaultdict(lambda: float("inf"))
    prev = defaultdict(lambda: -1)
    neighbor = defaultdict(list)
    vertex = set(range(n))
    for a, b, cost in edges:
        neighbor[a].append((b, cost))
        neighbor[b].append((a, cost))

    distances[0] = 0
    while vertex:
        node = min([(distances[i], i) for i in vertex])[1]
        vertex.remove(node)
        for adj_v, cost in neighbor[node]:
            alt = distances[node] + cost
            if alt < distances[adj_v]:
                distances[adj_v] = alt
                prev[adj_v] = node

    return distances[n - 1], back_trace(prev, n - 1)


def shortest(n, edges):
    """
    Given an undirected graph, find the shortest path from source (node 0)
    to target (node n-1).
    """
    heap_queue = heapdict({i: float("inf") for i in xrange(n)})
    neighbor, prev = defaultdict(list), defaultdict(lambda: -1)
    target = n - 1
    heap_queue[0] = 0

    for a, b, cost in edges:
        neighbor[a].append((b, cost))
        neighbor[b].append((a, cost))

    while heap_queue:
        node, dist = heap_queue.popitem()
        if node == target:
            return dist, back_trace(prev, target)
        for adj_v, cost in neighbor[node]:
            tmp = dist + cost
            if adj_v in heap_queue and tmp < heap_queue[adj_v]:
                heap_queue[adj_v] = tmp
                prev[adj_v] = node


def back_trace(prev, target):
    res = []
    while target > -1:
        res.append(target)
        target = prev[target]
    return list(reversed(res))


if __name__ == '__main__':
    print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
