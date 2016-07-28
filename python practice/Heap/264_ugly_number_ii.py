# -*- coding: utf-8 -*-
# 264. Ugly Number II
# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Note that 1 is typically treated as an ugly number.

# Hint:

# The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
# An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
# The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
# Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        i, j, k = 0, 0, 0
        uglys = [1]
        while n > 1:
            ugly2 = 2 * uglys[i]
            ugly3 = 3 * uglys[j]
            ugly5 = 5 * uglys[k]

            new_ugly = min(ugly2, ugly3, ugly5)

            if new_ugly == ugly2:
                i += 1
            if new_ugly == ugly3:
                j += 1
            if new_ugly == ugly5:
                k += 1
            n -= 1
            uglys.append(new_ugly)
        return uglys[len(uglys) - 1]

