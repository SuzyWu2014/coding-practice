# 268. Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sum = reduce(lambda x, y: x + y, nums)
        real_sum = (1 + len(nums)) * len(nums) / 2
        return real_sum - nums_sum

    def missingNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype
        0 ^ a = a， 以及 a ^ b ^ a = b
        """
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res

print Solution().missingNumber2([0, 1])
