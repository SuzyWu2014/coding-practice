# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t = dict()
        t_s = dict()
        for i, j in zip(s, t):
            if i in s_t and s_t[i] != j:
                    return False
            elif j in t_s and t_s[j] != i:
                    return False
            else:
                s_t[i] = j
                t_s[j] = i
        return True

print Solution().isIsomorphic('ab', 'aa')
