# 244. Shortest Word Distance II

# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
import collections


class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.words_idx = collections.defaultdict(list)
        for idx, word in enumerate(words):
            self.words_idx[word].append(idx)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_list, word2_list = self.words_idx[word1], self.words_idx[word2]
        min_diff = sys.maxsize
        i, j = 0, 0
        while i < len(word1_list) and j < len(word2_list):
            min_diff = min(min_diff, abs(word1_list[i] - word2_list[j]))
            if word1_list[i] < word2_list[j]:
                i += 1
            else:
                j += 1
        return min_diff

    def shortest2(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min([abs(i - j) for i in self.words_idx[word1] for j in self.words_idx[word2]])


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")