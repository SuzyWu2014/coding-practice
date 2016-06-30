# 204. Count Primes

# Description:

# Count the number of prime numbers less than a non-negative number, n.
import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        if n <= 3:
            return n - 2
        count = 2
        for i in range(4, n):
            if self.is_prime(i):
                count += 1
        return count

    def is_prime(self, n):
        end = int(math.sqrt(n)) + 1  # math.sqrt is expensive
        for i in range(2, end):
            if n % i == 0:
                return False
        return True


class Solution2(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True] * max(n, 2)
        is_prime[0], is_prime[1] = False, False
        i = 2
        while i * i < n:
            if is_prime[i]:
                next_not_prime = i * i
                while next_not_prime < n:
                    is_prime[next_not_prime] = False
                    next_not_prime += i
            i += 1
        return sum(is_prime)


print Solution2().countPrimes(499979)
