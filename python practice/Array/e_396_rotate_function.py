# 396. Rotate Function
# Given an array of integers A and let n to be its length.

# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

# Calculate the maximum value of F(0), F(1), ..., F(n-1).

# Note:
# n is guaranteed to be less than 105.

# Example:

# A = [4, 3, 2, 6]

# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
import sys


class Solution(object):

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None or A == []:
            return 0
        F = [0] * len(A)
        F[0] = sum([x * y for x, y in zip(A, range(len(A)))])
        sum_a = sum(A)
        for i in range(1, len(A)):
            F[i] = sum_a - len(A) * A[len(A) - i] + F[i - 1]
        return max(F)


    def maxRotateFunction2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None or A == []:
            return 0
        max_f = -sys.maxint - 1
        for i in range(len(A)):
            rotated = A[(len(A) - i):] + A[:(len(A) - i)]
            temp_sum = sum([x * y for x, y in zip(rotated, range(len(A)))])
            max_f = max(max_f, temp_sum)
        return max_f

print Solution().maxRotateFunction([4, 3, 2, 6])

