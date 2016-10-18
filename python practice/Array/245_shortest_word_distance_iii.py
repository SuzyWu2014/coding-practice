# 245. Shortest Word Distance III
# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# word1 and word2 may be the same and they represent two individual words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = "makes", word2 = "makes", return 3.

# Note:
# You may assume word1 and word2 are both in the list.
import collections


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        words_idx = collections.defaultdict(list)
        for idx, word in enumerate(words):
            words_idx[word].append(idx)

        if word1 == word2:
            idx_list = words_idx[word1]
            return min([idx_list[i] - idx_list[i - 1] for i in xrange(1, len(idx_list))])
        else:
            list1, list2 = words_idx[word1], words_idx[word2]
            i, j, res = 0, 0, sys.maxsize
            while i < len(list1) and j < len(list2):
                res = min(res, abs(list1[i] - list2[j]))
                if list1[i] < list2[j]:
                    i += 1
                else:
                    j += 1
            return res
