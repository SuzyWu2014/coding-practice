from msort import *
from inversions import *
from longest import *

# print mergesort(None)
# print mergesort([])
# print mergesort([1])
# print mergesort([2,1])
# print mergesort([2,1,2,1,2,1,2,1])
# print mergesort([2,1,3,4,7,2,1])


# print num_inversions(None)
# print num_inversions([2,1])
# print num_inversions([4, 1, 3, 2])
# print num_inversions([2, 4, 1, 3])

print longest(None)
print longest([])
print longest([[], 1, []])
print longest([[[], 1, []], 2, [[], 3, []]])
print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))
print(longest([[[], 1, []], 2, [[], 3, []]]))
print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[[[], 11,[]], 10, [[], 12, [[], 13,[]]]], 5, []], 6, [[], 7, [[], 9, []]]]]))
print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[[[], 11,[]], 10, [[], 12, [[], 13,[]]]], 5, []], 6, [[], 7, [[], 9, [[[], 15, []], 14, [[[], 17, []], 16, []]]]]]]))
