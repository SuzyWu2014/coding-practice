# -*- coding: utf-8 -*-
# 200. Number of Islands
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        dfs
        """
        if grid is None or len(grid) == 0:
            return 0
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    res += 1
        return res

    def dfs(self, row, col, grid):
        grid[row][col] = '0'

        if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
            self.dfs(row, col + 1, grid)
        if col - 1 >= 0 and grid[row][col - 1] == '1':
            self.dfs(row, col - 1, grid)
        if row + 1 < len(grid) and grid[row + 1][col] == '1':
            self.dfs(row + 1, col, grid)
        if row - 1 >= 0 and grid[row - 1][col] == '1':
            self.dfs(row - 1, col, grid)


    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        bfs
        """
        if grid is None or len(grid) == 0:
            return 0
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    queue.append([i, j])
                    grid[i][j] = '0'
                    while queue:
                        [row, col] = queue.pop(0)

                        if row + 1 < rows and grid[row + 1][col] == '1':
                            queue.append([row + 1, col])
                            grid[row + 1][col] = '0'
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            queue.append([row - 1, col])
                            grid[row - 1][col] = '0'
                        if col + 1 < cols and grid[row][col + 1] == '1':
                            queue.append([row, col + 1])
                            grid[row][col + 1] = '0'
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            queue.append([row, col - 1])
                            grid[row][col - 1] = '0'
                    res += 1
        return res

print Solution().numIslands2([list("11110"), list("11010"), list("11000"), list("00000")])

