# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Subscribe to see which companies asked this question


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        for i in range(1, row):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for j in range(1, col):
            grid[0][j] = grid[0][j - 1] + grid[0][j]
        for i in range(1, row):
            for j in range(1, col):
                if grid[i][j - 1] < grid[i - 1][j]:
                    grid[i][j] = grid[i][j] + grid[i][j - 1]
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
        return grid[row - 1][col - 1]
