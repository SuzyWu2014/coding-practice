# 367. Valid Perfect Square
# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Returns: True
# Example 2:

# Input: 14
# Returns: False


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        i = num / 2
        while i > 1 or i < num / 2:
            if i * i == num:
                return True
            elif i * i > num:
                i /= 2
            elif (i + 1) * (i + 1) > num:
                break
            else:
                i += 1
        return False


print Solution().isPerfectSquare(4)
print Solution().isPerfectSquare(49)
print Solution().isPerfectSquare(81)
print Solution().isPerfectSquare(82)
