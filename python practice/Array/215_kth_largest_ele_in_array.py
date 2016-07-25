# -*- coding: utf-8 -*-
# 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3, 2, 1, 5, 6, 4] and k = 2, return 5.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.120_triangle.py
import heapq
import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        O(nlog(n))
        """
        return sorted(nums, reversed=True)[k - 1]

    def findKthLargest2(self, nums, k):
        heap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(heap, nums[i])
            elif nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
            print heap, heap[0], heap[len(heap) - 1]
        return heapq.heappop(heap)

    def findKthLargest3(self, nums, k):
        # O(n)
        pivot = random.choice(nums)
        smallers, largers = [], []
        for num in nums:
            if num < pivot:
                smallers.append(num)
            if num > pivot:
                largers.append(num)
        if k <= len(largers):
            return self.findKthLargest3(largers, k)
        elif k > len(nums) - len(smallers):
            return self.findKthLargest3(smallers, k - (len(nums) - len(smallers)))
        else:
            return pivot


print Solution().findKthLargest3([-1, 2, 0], 2)
# print Solution().findKthLargest3([3, 2, 1, 5, 6, 4], 2)
# print Solution().findKthLargest2([2, 1], 2)
# print Solution().findKthLargest2([2, 1], 1)
