# 207. Course Schedule
# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# topology sort

import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        Topological sort => BFS
        """
        zero_pre = set()
        pres_count = [0] * numCourses
        for pre in prerequisites:
            pres_count[pre[0]] += 1
        for i in range(len(pres_count)):
            if pres_count[i] == 0:
                zero_pre.add(i)
        if not zero_pre:
            return False

        while zero_pre:
            it = iter(zero_pre)
            course = it.next()
            zero_pre.remove(course)

            for i in range(len(prerequisites)):
                pre = prerequisites[i]
                if pre[1] == course:
                    pres_count[pre[0]] -= 1
                    if pres_count[pre[0]] == 0:
                        zero_pre.add(pre[0])
        return sum(pres_count) == 0

    def canFinish2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        DFS
        """
        

