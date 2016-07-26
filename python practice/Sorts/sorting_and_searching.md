# p 179
# 1 You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

Merge part of the merge sort

# 2 Write a method to sort an array of strings so that all the anagrams are next to each other.

The basic idea is to implement a normal sorting algorithm where you override the compareTo method to compare the “signature” of each string. In this case, the signature is the alphabetically sorted string.

# 3 Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally sorted in increasing order.
# EXAMPLE:
# Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
# Output: 8 (the index of 5 in the array)

Modified binary search

# 4 If you have a 2 GB file with one string per line, which sorting algorithm would you use to sort the file and why?

When an interviewer gives a size limit of 2GB, it should tell you something - in this case, it suggests that they don’t want you to bring all the data into memory.
So what do we do? We only bring part of the data into memory..
Algorithm:
How much memory do we have available? Let’s assume we have X MB of memory available.
1. Divide the file into K chunks, where X * K = 2 GB. Bring each chunk into memory and sort the lines as usual using any O(n log n) algorithm. Save the lines back to the file.
2. Now bring the next chunk into memory and sort.
3. Once we’re done, merge them one by one.

# 5 Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.

Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] will return 4
Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return -1

Use ordinary binary search, but when you hit an empty string, advance to the next non-empty string; if there is no next non-empty string, search the left half.

<!--  9.7 A circus is designing a tower routine consisting of people standing atop one another’s shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.
EXAMPLE:
Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190) -->

Step 1. Sort all items by height first, and then by weight. This means that if all the heights are unique, then the items will be sorted by their height. If heights are the same, items will be sorted by their weight.
Example:
»»Before sorting: (60, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68,110).
»»After sorting: (56, 90), (60, 95), (60,100), (68, 110), (70,150), (75,190).

Step 2. Find the longest sequence which contains increasing heights and increasing weights.
To do this, we:
a) Start at the beginning of the sequence. Currently, max_sequence is empty.
b) If, for the next item, the height and the weight is not greater than those of the previous item, we mark this item as “unfit” .
(60,95)
(65,100)
(75,80)
(80, 100)
(unfit item)
c) If the sequence found has more items than “max sequence”, it becomes “max sequence”.
d) After that the search is repeated from the “unfit item”, until we reach the end of the original sequence.
