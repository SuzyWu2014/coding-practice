# 120. Triangle
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
import copy


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        paths = [0 for i in range(n)]
        paths[0] = triangle[0][0]
        tmp = [0 for i in range(n)]
        for i in range(1, n):
            tmp[0] = triangle[i][0] + paths[0]
            length = len(triangle[i])
            for j in range(1, length - 1):
                tmp[j] = min(paths[j - 1], paths[j]) + triangle[i][j]
            tmp[length - 1] = triangle[i][length - 1] + paths[length - 2]
            paths = copy.copy(tmp)
        return min(paths)

print Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])
