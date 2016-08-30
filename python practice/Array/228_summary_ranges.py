# 228. Summary Ranges
# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        rst = []
        while i < len(nums):
            start, num_str = i, str(nums[i])
            while i + 1 < len(nums) and nums[i] + 1 == nums[i +1]:
                i += 1
            if i > start:
                num_str += '->' + str(nums[i])
            rst.append(num_str)
            i += 1
        return rst
