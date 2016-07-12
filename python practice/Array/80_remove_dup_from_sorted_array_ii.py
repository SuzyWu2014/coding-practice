# 80. Remove Duplicates from Sorted Array II
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        i, j = 1, 2
        while i < len(nums) - 1 and j < len(nums):
            if nums[j] != nums[i - 1]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1
