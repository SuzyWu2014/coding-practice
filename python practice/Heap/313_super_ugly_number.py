# -*- coding: utf-8 -*-
# 313. Super Ugly Number
# Write a program to find the nth super ugly number.

# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        super_uglys = [1]
        idx = [0] * len(primes)
        while n > 1:
            new_uglys = []
            for i in range(len(idx)):
                new_uglys.append(super_uglys[idx[i]] * primes[i])
            ugly = min(new_uglys)
            for i in range(len(new_uglys)):
                if new_uglys[i] == ugly:
                    idx[i] += 1
            super_uglys.append(ugly)
            n -= 1
        return super_uglys[-1]


    def nthSuperUglyNumber2(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        faster
        """
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

print Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])
