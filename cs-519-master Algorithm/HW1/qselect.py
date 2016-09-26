#!/usr/bin/env python
import random


def qselect(k, nums):
    """
    Find the kth smallest element in the array
    """
    if k <= 0 or nums is None or k > len(nums):
        return
    pivot = random.choice(nums)
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]
    if k <= len(left):
        return qselect(k, left)
    elif k > len(nums) - len(right):
        return qselect(k - (len(nums) - len(right)), right)
    else:
        return pivot
