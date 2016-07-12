# 26. Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        i, j = 0, 1
        while i < len(nums) - 1 and j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1
