# -*- coding: utf-8 -*-
# 347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
            O(n * log k)
        """
        counts = collections.Counter(nums)
        heap = []
        for key, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, key))
            elif heap[0][0] < count:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, key))
        return [item[1] for item in heap]

    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
            O(n)
        """
        length = len(nums)
        countDict = collections.defaultdict(int)
        for i in nums:
            countDict[i] += 1
        freqList = [[] for i in range(length + 1)]
        for p in countDict:
            freqList[countDict[p]] += p,
        ans = []
        for p in range(length, 0, -1):
            ans += freqList[p]
        return ans[:k]

print Solution().topKFrequent2([1, 1, 1, 2, 2, 3], 2)
