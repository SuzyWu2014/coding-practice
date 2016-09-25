#!/usr/bin/env python
import random


def qselect(k, nums):
    """
    Find the kth smallest element in the array
    """
    pivot = random.choice(nums)
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]
    if k <= len(left):
        return qselect(k, left)
    elif k > len(nums) - len(right):
        return qselect(k - (len(nums) - len(right)), right)
    else:
        return pivot

# best-case: O(n) -> O(n) for partition, then get the result after 1 round
# worse-case: O(n^2)
# average-case: O(n)
