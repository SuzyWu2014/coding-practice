# 49. Group Anagrams
# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = dict()
        for word in strs:
            w = ''.join(sorted(word))
            if w not in word_dict:
                word_dict[w] = [word]
            else:
                word_dict[w].append(word)
        return word_dict.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
