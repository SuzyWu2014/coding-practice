# 364. Nested List Weight Sum II
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

# Example 1:
# Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

# Example 2:
# Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import collections


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or nestedList == []:
            return 0
        level_dict = collections.defaultdict(list)
        self.dfs(nestedList, level_dict, 1)
        if len(level_dict) == 0:
            return 0
        else:
            depth = max(level_dict.keys())
        diff = depth - len(level_dict) + 1 if depth > len(level_dict) else 1
        total = 0
        for level in level_dict:
            # print level, level_dict[level], len(level_dict) - level + diff
            total += sum(level_dict[level]) * (len(level_dict) - level + diff)
        return total

    def dfs(self, nestedList, level_dict, level):
        for i in xrange(len(nestedList)):
            if nestedList[i].isInteger():
                level_dict[level].append(nestedList[i].getInteger())
            else:
                self.dfs(nestedList[i].getList(), level_dict, level + 1)
