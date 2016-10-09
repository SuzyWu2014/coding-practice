# 392. Is Subsequence  QuestionEditorial Solution  My Submissions
# Total Accepted: 10512
# Total Submissions: 23850
# Difficulty: Medium
# Given a string s and a string t, check if s is subsequence of t.

# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# s = "abc", t = "ahbgdc"

# Return true.

# Example 2:
# s = "axc", t = "ahbgdc"

# Return false.

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = iter(t)
        return all(c in t for c in s)


    def isSubsequence2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        if t is None or len(s) > len(t):
            return False
        i, j = 0, 0
        while i < len(t):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    return True
            i += 1
        return False

    def isSubsequence3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        if t is None or len(s) > len(t):
            return False

        dp = [-1] * len(t)
        dp[0], j = (0, 1) if s[0] == t[0] else (-1, 0)
        i = 1
        while i < len(t):
            if t[i] == s[j]:
                dp[i] = j
                j += 1
                if j == len(s):
                    return True
            else:
                dp[i] = dp[i - 1]
            i += 1
        return dp[len(t) - 1] == len(s) - 1


print Solution().isSubsequence("axc", "csdsdahbgdc")
print Solution().isSubsequence("abc", "ahbgdc")
