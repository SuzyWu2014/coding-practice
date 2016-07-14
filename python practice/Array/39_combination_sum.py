# 39. Combination Sum
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]


class Solution(object):
    def DFS(self, candidates, target, start, value_list):
        length = len(candidates)
        if target == 0:
            return self.rst.append(value_list)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, value_list + [candidates[i]])

    def combinationSum(self, candidates, target):
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
