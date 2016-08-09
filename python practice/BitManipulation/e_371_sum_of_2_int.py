# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3.


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        RuntimeError: maximum recursion depth exceeded in cmp
        """
        result = a ^ b
        carry = (a & b) << 1
        if carry != 0:
            return self.getSum(result, carry)
        else:
            return result

    def getSum2(self, a, b):
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b != 0:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
