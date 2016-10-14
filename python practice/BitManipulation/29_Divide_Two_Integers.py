# 29. Divide Two Integers
# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        if divisor == 0:
            return MAX_INT

        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        current = divisor
        current_result = 1
        while current <= dividend:
            current <<= 1
            current_result <<= 1

        while divisor <= dividend:
            current >>= 1
            current_result >>= 1
            if current <= dividend:
                dividend -= current
                result += current_result
        return min(sign * result, MAX_INT)


if __name__ == "__main__":
    print Solution().divide(5, -1)
    # assert Solution().divide(10, 2) == 5
