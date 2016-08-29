# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".

# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".

# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.


class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        elements = [0] * n
        for i, s in enumerate(words):
            for c in s:
                elements[i] |= 1 << (ord(c) - 97) # 1 shift left for n bits
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not (elements[i] & elements[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])



