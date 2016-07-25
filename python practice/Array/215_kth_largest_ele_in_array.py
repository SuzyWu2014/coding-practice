# -*- coding: utf-8 -*-
# 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3, 2, 1, 5, 6, 4] and k = 2, return 5.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.120_triangle.py
import heapq


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

print Solution().findKthLargest2([3, 2, 1, 5, 6, 7, 4], 4)
# print Solution().findKthLargest2([2, 1], 2)
# print Solution().findKthLargest2([2, 1], 1)
