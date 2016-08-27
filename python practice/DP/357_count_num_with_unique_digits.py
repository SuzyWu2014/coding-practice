# -*- coding: utf-8 -*-
# 357. Count Numbers with Unique Digits
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

# Show Hint


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        n = min(10, n)
        cnt = [9] * n
        cnt[0] = 10
        for i in range(1, n):
            for j in range(9, 10 - i - 1, -1):
                cnt[i] *= j
        return sum(cnt)

    def countNumbersWithUniqueDigits2(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [9]
        for x in range(9, 0, -1):
            nums += nums[-1] * x,

        return sum(nums[:n]) + 1

print Solution().countNumbersWithUniqueDigits2(3)

