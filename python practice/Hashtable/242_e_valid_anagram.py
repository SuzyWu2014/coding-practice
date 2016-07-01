# *-- encoding: utf-8 --*
# 242. Valid Anagram
# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    @profile
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        list_s = sorted(s)
        list_t = sorted(t)
        if list_s == list_t:
            return True
        else:
            return False

if __name__ == "__main__":
    print(Solution().isAnagram(u'我们', u'而我'))
