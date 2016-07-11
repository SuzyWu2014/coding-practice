# 18. 4Sum
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_len, rst, sum_dict = len(nums), set(), dict()
        if nums_len <= 3:
            return []
        nums.sort()
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] not in sum_dict:
                    sum_dict[nums[i] + nums[j]] = [(i, j)]
                else:
                    sum_dict[nums[i] + nums[j]].append((i, j))

        for i in range(nums_len):
            for j in range(i + 1, nums_len - 2):
                t = target - nums[i] - nums[j]
                if t in sum_dict:
                    for k in sum_dict[t]:
                        if k[0] > j:
                            rst.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in rst]

# 解题思路：
"""
四个数和为0，先排序：
1， 求两个数的和的所有结果存在dict里，key为和，value为两个数的位置
2， 重新计算任意两个数之和，并check 对应的和的负数是否已经在dict中
"""
