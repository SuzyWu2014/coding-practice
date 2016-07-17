# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?
# Note: m and n will be at most 100.


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        dp_table = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp_table[0][i] = 1
        for j in range(m):
            dp_table[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp_table[i][j] = dp_table[i][j - 1] + dp_table[i - 1][j]
        return dp_table[m - 1][n - 1]


print Solution().uniquePaths(3, 7)


# paths = [[1] for i in range(m)]  # initialize the 1st column to be 1
# for i in range(n - 1):           # initialize the 1st row to be 1
#     paths[0].append(1)