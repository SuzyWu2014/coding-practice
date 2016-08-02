# 43. Multiply Strings
# Given two numbers represented as strings, return multiplication of the numbers as a string.

# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        digit_sum = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit_sum[i + j] += int(num1[i]) * int(num2[j])
        ans = []
        for i in range(len(digit_sum)):
            digit = digit_sum[i] % 10
            carry = digit_sum[i] / 10
            if i < len(digit_sum) - 1:
                digit_sum[i + 1] += carry
            ans.insert(0, str(digit))
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        return ''.join(ans)
