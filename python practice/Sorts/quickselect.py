# -*- coding: utf-8 -*-
# Quickselect
# 用于快速找出 Kth smallest element from unsorted array
# 为随机算法

# 基本思路：
# 从数组中随机取一个数作为pivot
# 将数组分为左右两个部分left, right based on pivot
# 确认 Kth element 在左右那个数组
# 递归寻找
# 注意点：pivot 值可能不是unique

import random


def quickSelect(nums, k):
    pivot = random.choice(nums)
    smallers, largers = [], []
    for num in nums:
        if num < pivot:
            smallers.append(num)
        elif num > pivot:
            largers.append(num)

    if k <= len(smallers):
        return quickSelect(smallers, k)
    elif k > len(nums) - len(largers):
        # could be multiple nums == pivot
        return quickSelect(largers, k - (len(nums) - len(largers)))
    else:
        return pivot

print quickSelect([3, 2, 1, 5, 6, 7, 4], 6)
