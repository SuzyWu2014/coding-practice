from collections import defaultdict, deque
from enum import Enum


def order(n, edges):
    """
    For a given directed graph, output a topological order if it exists.
    Tie-breaking: whenever you have a choice of vertices to explore,
        always pick the one with the smallest id.
    @n: the number of nodes
    @edges: a list of pairs representing edges
    BFS
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


def order_dfs_recursive(n, edges):
    """
    For a given directed graph, output a topological order if it exists.
    Tie-breaking: whenever you have a choice of vertices to explore,
        always pick the one with the smallest id.
    @n: the number of nodes
    @edges: a list of pairs representing edges

    dfs - O(|E| + |V|)
    """
    State = Enum('NOT_VISITED','VISITING', 'VISITED')
    res = deque()
    visited = defaultdict(lambda: State.NEVER_VISITED)
    outgoing = defaultdict(list)
    for a, b in edges:
        outgoing[a].append(b)

    def visit(node):
        visited[node] = State.VISITING
        for next_node in outgoing[node]:
            if visited[next_node] == State.VISITING:
                break
            if visited[next_node] == State.NOT_VISITED:
                visit(next_node)
        else:
            res.appendleft(node)
            visited[node] = State.VISITED

    for i in xrange(n):
        if visited[i] == State.NOT_VISITED:
            visit(i)

    return None if len(res) < n else list(res)


def order_dfs_non_recursive(n, edges):
    """
    For a given directed graph, output a topological order if it exists.
    Tie-breaking: whenever you have a choice of vertices to explore,
        always pick the one with the smallest id.
    @n: the number of nodes
    @edges: a list of pairs representing edges

    dfs - O(|E| + |V|)
    """
    stack = []
    res = deque()
    State = Enum("Visiting", "Visited", "NotVisited")
    outgoing = defaultdict(list)
    visit = defaultdict(lambda: State.NotVisited)

    for a, b in edges:
        outgoing[a].append(b)

    for node in xrange(n):
        if visit[node] == State.NotVisited:
            stack.append(node)
            while stack:
                curr = stack[-1]
                if len(outgoing[curr]) == 0 or all( x in res for x in outgoing[curr]):
                    curr = stack.pop()
                    res.appendleft(curr)
                    visit[curr] = State.Visited
                else:
                    visit[curr] = State.Visiting
                    for adj_v in outgoing[curr]:
                        if visit[adj_v] == State.Visiting:
                            return None
                        if visit[adj_v] == State.NotVisited:
                            stack.append(adj_v)
    return list(res)


if __name__ == '__main__':
    print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,7), (5,6)])
    print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
    print order(8, [(6,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,0), (5,7)])
    print order(8, [(3,2), (1,2), (2,0), (2,4), (0,4), (0,5), (5,6), (5,7)])
    print order(5, [(2,1), (1,3), (3,4), (2,3), (4, 0), (1, 0)])
    print order(5, [(2,1), (1,3), (3,4), (2,3), (4, 0), (1, 0), (4, 1)])
    print order(4, [(0,1), (1,2), (2,1), (2,3)])
    print order(2, [(1,0), (0,1)])
