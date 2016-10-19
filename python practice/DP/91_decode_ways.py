# 91. Decode Ways
# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0 or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        # dp[0] empty string
        dp = [1,1]
        for i in xrange(2, len(s) + 1):
            tmp_rst = 0
            sub = s[i - 2: i]
            sub = int(sub) if sub[0] != "0" else -1
            if s[i - 1] == "0" and sub == -1:
                return 0
            if s[i - 1] != "0":
                tmp_rst += dp[i - 1]
            if sub >= 10 and sub <= 26:
                tmp_rst += dp[i - 2]
            dp.append(tmp_rst)

        return dp[len(s)]

    def numDecodings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0 or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * len(s)
        dp[0] = 1

        sub = int(s[:2])
        if s[1] == "0":
            if sub > 26:
                return 0
            else:
                dp[1] = 1
        elif sub >= 10 and sub <= 26:
            dp[1] = 2
        else:
            dp[1] = 1

        for i in xrange(2, len(s)):
            tmp_rst = 0
            sub = s[i - 1: i + 1]
            sub = int(sub) if sub[0] != "0" else -1
            if s[i] == "0" and sub == -1:
                return 0
            if s[i] != "0":
                tmp_rst += dp[i - 1]
            if sub >= 10 and sub <= 26:
                tmp_rst += dp[i - 2]
            dp[i] = tmp_rst

        return dp[len(s) - 1]


# if "__name__" == "main":
print Solution().numDecodings("10")
print Solution().numDecodings("102")
print Solution().numDecodings("1020")
print Solution().numDecodings("12")
print Solution().numDecodings("1224")
