# 15. 3Sum
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        rst.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left - 1]:
                                break
                    else:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right + 1]:
                                break
        return rst

# 解题思路
"""
求三个数之和为0的组合：
1，求和题基本先排序
2，以第 i 个数为基点，求两个数之和为 - nums[i]
3, 注意找到后，相邻数字相同的情况
"""
