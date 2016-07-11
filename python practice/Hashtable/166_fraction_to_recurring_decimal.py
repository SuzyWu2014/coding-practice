# 166. Fraction to Recurring Decimal
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        is_negative = numerator * denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        integer_str = str(numerator / denominator)
        if is_negative:
            integer_str = "-" + integer_str
        numerator = numerator % denominator
        if numerator == 0:
            return integer_str
        remainder_dict = dict()
        rst, decimal_position, decimal_str = [], 0, None
        remainder_dict[numerator] = 0
        while 1:
            decimal_position += 1
            quotient = numerator * 10 / denominator
            numerator = numerator * 10 % denominator
            rst.append(quotient)
            if numerator == 0:
                decimal_str = "".join([str(i) for i in rst])
                break
            if numerator not in remainder_dict:
                remainder_dict[numerator] = decimal_position
            else:
                loop_pos = remainder_dict[numerator]
                loop_str = "".join([str(i) for i in rst[loop_pos:]])

                decimal_str = "".join([str(i) for i in rst[:loop_pos]]) + "(" + loop_str + ")"
                break
        return integer_str + "." + decimal_str

print Solution().fractionToDecimal(1, 6)
print Solution().fractionToDecimal(1, 3)
print Solution().fractionToDecimal(4, 3)

# 解题思路
"""
使用原始的求余数的方法
hash部分：dict 存余数，及相应的小数位置
"""
