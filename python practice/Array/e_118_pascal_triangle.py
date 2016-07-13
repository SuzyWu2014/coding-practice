# 118. Pascal's Triangle
# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#  [1],
#  [1,1],
#  [1,2,1],
#  [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rst = [0] * numRows
        for i in range(numRows):
            if i == 0:
                rst[i] = [1]
            elif i == 1:
                rst[i] = [1, 1]
            else:
                rst[i] = [0] * (i + 1)
                rst[i][0] = rst[i][i] = 1
                for j in range(1, i):
                    rst[i][j] = rst[i - 1][j - 1] + rst[i - 1][j]
        return rst
