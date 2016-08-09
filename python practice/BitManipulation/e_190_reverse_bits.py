# 190. Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

# Follow up:
# If this function is called many times, how would you optimize it?

# Related problem: Reverse Integer


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans
