# *--encoding: utf-8 ---*
# 229. Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

# Hint:

# How many majority elements could it possibly have?

#  https://segmentfault.com/a/1190000003972762


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        num1, num2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num1 == num:
                count1 += 1
            elif num2 == num:
                count2 += 1
            elif count1 == 0:
                num1, count1 = num, 1
            elif count2 == 0:
                num2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        print num1, num2
        return [n for n in (num1, num2)
                if n is not None and nums.count(n) > len(nums) / 3]


# Solution().majorityElement([6, 6, 6, 7, 7])

Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2])
