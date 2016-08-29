# 378. Kth Smallest Element in a Sorted Matrix
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        heap, only if j == 0, move downwards
        """
        heap = [(matrix[0][0], 0, 0)]
        for _ in range(k):
            rst, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix) and j == 0:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return rst


    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        binary search
        """
        
