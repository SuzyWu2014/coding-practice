# 53. Maximum Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.

# click to show more practice.

# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        max_sum = pre_sum = nums[0]
        for i in range(1, len(nums)):
            if pre_sum + nums[i] < nums[i]:
                start = i
                pre_sum = nums[i]
            else:
                pre_sum = pre_sum + nums[i]
            if pre_sum > max_sum:
                max_sum = pre_sum
                end = i
        return max_sum
