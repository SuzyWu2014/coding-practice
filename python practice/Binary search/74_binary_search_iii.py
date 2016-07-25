# 74. Search a 2D Matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols - 1
        up, down = 0, rows - 1
        while left <= right and up <= down:
            mid_row = (up + down) / 2
            mid_col = (left + right) / 2
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                if matrix[mid_row][cols - 1] < target:
                    up = mid_row + 1
                else:
                    up = down = mid_row
                    left = mid_col + 1
            else:
                if matrix[mid_row][0] > target:
                    down = mid_row - 1
                else:
                    up = down = mid_row
                    right = mid_col - 1
        return False

print Solution().searchMatrix([[1, 1]], 2)
