# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = 0
        sub_str_left = 0
        char_prev_pos = dict()
        for i in range(len(s)):
            if s[i] in char_prev_pos and char_prev_pos[s[i]] >= sub_str_left:
                sub_str_left = char_prev_pos[s[i]] + 1
            char_prev_pos[s[i]] = i
            rst = max(rst, i - sub_str_left + 1)
        return rst

print Solution().lengthOfLongestSubstring("a")
print Solution().lengthOfLongestSubstring("au")
print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("bbbbb")
print Solution().lengthOfLongestSubstring("aab")
print Solution().lengthOfLongestSubstring("pwwkew")
