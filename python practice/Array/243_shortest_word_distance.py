# -*- coding: utf-8 -*-
# 243. Shortest Word Distance
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = -1, -1
        rst = len(words)
        for idx, word in enumerate(words):
            if word == word1:
                idx1 = idx
                if idx2 != -1:
                    rst = min(rst, abs(idx1 - idx2))
            elif word == word2:
                idx2 = idx
                if idx1 != -1:
                    rst = min(rst, abs(idx1 - idx2))
        return rst

    def shortestDistance2(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_idx, word2_idx = [], []
        for idx, word in enumerate(words):
            if word == word1:
                word1_idx.append(idx)
            elif word == word2:
                word2_idx.append(idx)
        # print word1_idx, word2_idx
        return min([abs(i - j) for i in word1_idx for j in word2_idx])



print(Solution().shortestDistance(["a","c","b","b","a"], "a", "b"))
print(Solution().shortestDistance(["a","a","b","b"], "a", "b"))