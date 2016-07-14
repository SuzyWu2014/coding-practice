# 40. Combination Sum II
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]


class Solution(object):
    def DFS(self, candidates, target, start, value_list):
        length = len(candidates)
        if target == 0 and value_list not in Solution.rst:
            return self.rst.append(value_list)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i + 1, value_list + [candidates[i]])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.rst = []
        self.DFS(candidates, target, 0, [])
        return self.rst

print Solution().combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
