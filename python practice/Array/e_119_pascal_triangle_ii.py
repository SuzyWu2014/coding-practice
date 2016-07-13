# 119. Pascal's Triangle II
# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            pre_row = [1, 1]
            for i in range(2, rowIndex + 1):
                new_row = [0] * (i + 1)
                new_row[0] = new_row[i] = 1
                for j in range(1, i):
                    new_row[j] = pre_row[j - 1] + pre_row[j]
                pre_row = new_row
            return pre_row
