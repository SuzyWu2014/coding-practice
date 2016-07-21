# 16. 3Sum Closest
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = 100000
        res = 0
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                diff = abs(three_sum - target)
                if diff == 0:
                    return target
                if diff < min_diff:
                    min_diff = diff
                    res = three_sum
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        return res
