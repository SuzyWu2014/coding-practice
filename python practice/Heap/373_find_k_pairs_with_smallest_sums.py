# 373. Find K Pairs with Smallest Sums
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

# Return: [1,2],[1,4],[1,6]

# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
# Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

# Return: [1,1],[1,1]

# The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
# Given nums1 = [1,2], nums2 = [3],  k = 3

# Return: [1,3],[2,3]

# All possible pairs are returned from the sequence:
# [1,3],[2,3]
import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        k = min(k, len(nums1) * len(nums2))
        if k == 0:
            return []
        rst = []
        heap = []
        i, j = 0, 0
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        while len(rst) < k:
            min_sum, i, j = heapq.heappop(heap)
            rst.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return rst


print Solution().kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 3)
# print Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
# print Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 2)
# print Solution().kSmallestPairs([1, 2], [3], 3)
# print Solution().kSmallestPairs([], [], 3)

