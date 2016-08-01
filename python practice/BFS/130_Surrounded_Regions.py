# -*- coding: utf-8 -*-
# 130. Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# 解题思路：
# 找到边界上的0作为入口点，用dfs/bfs 将连接的0 替换为D
# 最后遍历board, 0 -> X, D -> O

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        dfs: RuntimeError: maximum recursion depth exceeded in cmp
        """
        if board is None or len(board) <= 2:
            return
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][cols - 1] == 'O':
                self.dfs(i, cols - 1, board)
        for j in range(cols):
            if board[0][j] == 'O':
                self.dfs(0, j, board)
            if board[rows - 1][j] == 'O':
                self.dfs(rows - 1, j, board)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] == 'X'
                elif board[i][j] == 'D':
                    board[i][j] == 'O'

    def dfs(self, row, col, board):
        board[row][col] = 'D'
        if row + 1 < len(board) and board[row + 1][col] == 'O':
            self.dfs(row + 1, col, board)
        if row - 1 > 0 and board[row - 1][col] == 'O':
            self.dfs(row - 1, col, board)
        if col + 1 < len(board[0]) and board[row][col + 1] == 'O':
            self.dfs(row, col + 1, board)
        if col - 1 < len(board) and board[row][col - 1] == 'O':
            self.dfs(row, col - 1, board)

    def solve2(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        dfs: RuntimeError: maximum recursion depth exceeded in cmp
        """
        if board is None or len(board) <= 2:
            return
        rows = len(board)
        cols = len(board[0])
        queue = []
        for i in range(rows):
            self.bfs(i, 0, board, queue)
            self.bfs(i, cols - 1, board, queue)
        for j in range(cols):
            self.bfs(0, j, board, queue)
            self.bfs(rows - 1, j, board, queue)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'
        print board

    def bfs(self, row, col, board, queue):
        if board[row][col] == 'O':
            self.fill(row, col, board, queue)
        while(queue):
            [r, c] = queue.pop(0)
            self.fill(r + 1, c, board, queue)
            self.fill(r - 1, c, board, queue)
            self.fill(r, c + 1, board, queue)
            self.fill(r, c - 1, board, queue)

    def fill(self, x, y, board, queue):
        if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1 or board[x][y] != 'O':
            return
        board[x][y] = 'D'
        queue.append([x, y])

Solution().solve2([list("OOO"), list("OOO"), list("OOO")])