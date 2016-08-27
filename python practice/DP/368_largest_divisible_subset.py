# 368. Largest Divisible Subset
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# nums: [1,2,3]

# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# nums: [1,2,4,8]

# Result: [1,2,4,8]


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums)
        pre = [None] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j
        idx = dp.index(max(dp))
        rst = []
        while idx is not None:
            rst.append(nums[idx])
            idx = pre[idx]
        return rst

# print Solution().largestDivisibleSubset([1, 2, 3])
print Solution().largestDivisibleSubset([1, 2, 4, 8])
print Solution().largestDivisibleSubset([1, 3, 2, 9, 4, 8])