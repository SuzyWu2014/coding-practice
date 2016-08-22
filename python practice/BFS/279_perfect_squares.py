# 279. Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
import collections
import sys
import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]

    def __init__(self):
        self.dp = [0]

    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(len(self.dp), n + 1):
            result = sys.maxsize
            k = int(math.sqrt(i))
            if k * k == i:
                self.dp.append(1)
                continue
            for j in range(1, int(math.sqrt(i)) + 1):
                result = min( self.dp[i - j * j] + 1, result)
                if result == 2:
                    break
            self.dp.append(result)
        return self.dp[n]

    def numSquares3(self, n):
        if n < 2:
            return n
        sqr_list = []
        i = 1
        while i * i <= n:
            sqr_list.append(i * i)
            i += 1
        to_check = {n}
        cnt = 0
        while to_check:
            cnt += 1
            next_to_check = set()
            for num in to_check:
                for item in sqr_list:
                    if num == item:
                        return cnt
                    if num < item:
                        break
                    next_to_check.add(num - item)
            to_check = next_to_check
        return cnt


print Solution().numSquares3(4)
