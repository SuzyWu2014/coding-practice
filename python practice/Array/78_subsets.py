# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        for num in nums:
            rst += [item + [num] for item in rst]
        return rst

    # slower
    def subsets2(self, nums):
        rst = []

        def dfs(depth, start, value_list):
            rst.append(value_list)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, value_list + [nums[i]])

        dfs(0, 0, [])
        return rst

print Solution().subsets([1, 2, 3])
