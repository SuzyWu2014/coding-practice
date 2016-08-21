# 345. Reverse Vowels of a String
# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        chars = list(s)
        while 1:
            while left < len(s) and chars[left].lower() not in "aeiou":
                left += 1
            while right > 0 and chars[right].lower() not in "aeiou":
                right -= 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            else:
                break
        return "".join(chars)

print Solution().reverseVowels(".,")
