#! -*- coding: utf-8 -*-

# 209. Minimum Size Subarray Sum
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

# click to show more practice.

# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        min_sub_len = len(nums) + 1
        curr_sum = 0
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= s:
                min_sub_len = min(right - left + 1, min_sub_len)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return 0 if min_sub_len > len(nums) else min_sub_len

print Solution().minSubArrayLen(7, [2,3,1,2,4,3])
