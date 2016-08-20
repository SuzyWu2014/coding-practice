# 66. Plus One
# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sub_sum = digits[i] + carry
            digits[i] = sub_sum % 10
            carry = sub_sum / 10
        if carry == 1:
            digits.insert(0, 1)
        return digits
