from collections import defaultdict, namedtuple


def shortest(n, edges):
    """
    Given an undirected graph, find the shortest path from source (node 0)
    to target (node n-1).
    """
    distances = defaultdict(lambda: float("inf"))
    pair = namedtuple("pair", "src dest")
    prev = defaultdict(lambda: -1)
    neighbor = defaultdict(list)
    vertex = set(range(n))
    for a, b, cost in edges:
        neighbor[a].append((b, cost))
        neighbor[b].append((a, cost))

    distances[0] = 0
    while vertex:
        node = min([(i, distances[i]) for i in vertex])[0]
        vertex.remove(node)
        for adj_v, cost in neighbor[node]:
            alt = distances[node] + cost
            if alt < distances[adj_v]:
                distances[adj_v] = alt
                prev[adj_v] = node

    return distances[n - 1], back_trace(prev, n)

def back_trace(prev, n):
    target = n - 1
    res = []
    while target > -1:
        res.append(target)
        target = prev[target]
    return list(reversed(res))


if __name__ == '__main__':
    print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
