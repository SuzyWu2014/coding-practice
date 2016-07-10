# 187. Repeated DNA Sequences
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# For example,

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
import collections


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seq_dict = collections.defaultdict(int)
        for i in range(len(s) - 9):
            key = s[i: i + 10]
            seq_dict[key] += 1
        return [sub_str for sub_str, count in seq_dict.iteritems() if count > 1]

print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
