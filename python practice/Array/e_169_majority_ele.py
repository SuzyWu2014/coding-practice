# 169. Majority Element
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.
import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        for key, value in count.iteritems():
            if value > len(nums) / 2:
                return key

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        for key, value in count.iteritems():
            if value > len(nums) / 2:
                return key
