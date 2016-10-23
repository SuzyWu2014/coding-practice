# 139. Word Break
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        62 ms
        """
        ok = [True]
        for i in xrange(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in wordDict for j in xrange(i)),
        return ok[-1]


if __name__ == '__main__':
    print(Solution().wordBreak("leetcode", set(["leet", "code"])))