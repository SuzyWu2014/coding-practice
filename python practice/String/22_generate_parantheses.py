# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, left, right, item, res):
        if right < left:
            return
        if left == 0 and right == 0:
            res.append(item)
        if left > 0:
            self.helper(left - 1, right, item + '(', res)
        if right > 0:
            self.helper(left, right - 1, item + ')', res)
