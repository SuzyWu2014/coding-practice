# 310. Minimum Height Trees
# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1:

# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3
# return [1]

# Example 2:

# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]

# Hint:

# How many MHTs can a graph have at most?
import collections


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if edges == []:
            return [0]
        children = collections.defaultdict(set)
        for s, t in edges:
            children[s].add(t)
            children[t].add(s)
        leaves = [x for x in range(n) if len(children[x]) == 1]
        while n > 2:
            # util less than 2 nodes left
            n -= len(leaves)
            new_leaves = []
            for leave in leaves:
                parent = children[leave].pop()
                children[parent].remove(leave)
                if len(children[parent]) == 1:
                    new_leaves.append(parent)
            leaves = new_leaves
        return leaves

print Solution().findMinHeightTrees(4, [[1,0], [1,2], [1,3]])
