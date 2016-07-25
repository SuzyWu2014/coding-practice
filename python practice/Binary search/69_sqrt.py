# 69. Sqrt(x)
# Implement int sqrt(int x).

# Compute and return the square root of x.


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        i, j = 1, x / 2 + 1
        while i <= j:
            mid = (i + j) / 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                j = mid - 1
            else:
                i = mid + 1
        return j

print Solution().mySqrt(2)
