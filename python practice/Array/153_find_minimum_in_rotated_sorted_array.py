# 153. Find Minimum in Rotated Sorted Array
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

    def findMin2(self, nums):
        return min(nums)

    def findMin3(self. nums):
        ans = nums[0]
        size = len(nums)
        low, high = 0, size - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]:
                # min位于左侧上升沿
                high = mid - 1
            else:
                # min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
            ans = min(ans, nums[mid])
        return ans
