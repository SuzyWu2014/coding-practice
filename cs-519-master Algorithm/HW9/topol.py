from collections import defaultdict, deque


def order(n, edges):
    """
    For a given directed graph, output a topological order if it exists.
    Tie-breaking: whenever you have a choice of vertices to explore,
        always pick the one with the smallest id.
    @n: the number of nodes
    @edges: a list of pairs representing edges

    Kahn's algorithm - O(|E| + |V|)
    """
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


if __name__ == '__main__':
    print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
    print order(4, [(0,1), (1,2), (2,1), (2,3)])
