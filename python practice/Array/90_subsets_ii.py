# 90. Subsets II
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        nums.sort()
        for num in nums:
            rst += [item + [num] for item in rst]
        ans = []
        for item in rst:
            if item not in ans:
                ans.append(item)
        return ans

    def subsetsWithDup2(self, nums):
        nums.sort()
        p = [[nums[x] for x in range(len(nums)) if i >> x & 1] for i in range(2**len(nums))]
        func = lambda x, y: x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))

    def subsetsWithDup3(self, nums):
        def dfs(depth, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, valuelist + [nums[i]])
        nums.sort()
        res = []
        dfs(0, 0, [])
        return res

    def subsetsWithDup4(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        nums.sort()
        for num in nums:
            rst += [item + [num] for item in rst if item + [num] not in rst]
        return rst
