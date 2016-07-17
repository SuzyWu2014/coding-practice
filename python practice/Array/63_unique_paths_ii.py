# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[row - 1][col - 1] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        for i in range(1, row):
            if obstacleGrid[i][0] == 1 or obstacleGrid[i - 1][0] == 0:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = 1
        for j in range(1, col):
            if obstacleGrid[0][j] == 1 or obstacleGrid[0][j - 1] == 0:
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = 1
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[row - 1][col - 1]


print Solution().uniquePathsWithObstacles([[0]])
