# 59. Spiral Matrix II
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []
        left, right = 0, n - 1
        up, down = 0, n - 1
        direction = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        num = 1
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    matrix[up][i] = num
                    num += 1
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    matrix[i][right] = num
                    num += 1
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = num
                    num += 1
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
            if num > n ** 2:
                return matrix
            direction = (direction + 1) % 4
