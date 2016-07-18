# 152. Maximum Product Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        pre_min, pre_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp_min = min(nums[i], nums[i] * pre_min, nums[i] * pre_max)
            pre_max = max(nums[i], nums[i] * pre_min, nums[i] * pre_max)
            pre_min = tmp_min
            max_product = max(max_product, pre_max)
        return max_product
