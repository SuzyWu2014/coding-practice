# 79. Word Search
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x, y, word):
            if len(word) == 0:
                return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x - 1, y, word[1:]):
                    return True
                board[x][y] = tmp

            # down
            if x < len(board) - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y - 1, word[1:]):
                    return True
                board[x][y] = tmp

            # right
            if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:]):
                        return True
        return False
