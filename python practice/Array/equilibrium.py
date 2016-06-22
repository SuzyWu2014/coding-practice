demoGQD96C-3AX
Python 00:08:15
Task description
You are currently in practice mode. This is a demo only.

A zero-indexed array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 ≤ P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices, i.e. 
A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.

For example, consider the following array A consisting of N = 8 elements:

  A[0] = -1
  A[1] =  3
  A[2] = -4
  A[3] =  5
  A[4] =  1
  A[5] = -6
  A[6] =  2
  A[7] =  1
P = 1 is an equilibrium index of this array, because:

A[0] = −1 = A[2] + A[3] + A[4] + A[5] + A[6] + A[7]
P = 3 is an equilibrium index of this array, because:

A[0] + A[1] + A[2] = −2 = A[4] + A[5] + A[6] + A[7]
P = 7 is also an equilibrium index, because:

A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = 0
and there are no elements with indices greater than 7.

P = 8 is not an equilibrium index, because it does not fulfill the condition 0 ≤ P < N.

Write a function:

def solution(A)

that, given a zero-indexed array A consisting of N integers, returns any of its equilibrium indices. The function should return −1 if no equilibrium index exists.

For example, given array A shown above, the function may return 1, 3 or 7, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.

Custom test cases		
Solution


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
def solution(A):
    # write your code in Python 2.7
    sum_a = sum(A) 
    if sum_a - A[0] == 0:
        return 0
    else:
        curr_sum = 0
        for i in range(len(A)-2):
            left = curr_sum + A[0]
            right = sum_a - left - A[i+1]
            if left == right:
                return i+1
        return -1
Python 2.7All changes saved.Keyboard shortcuts
Help     Run     Submit this task  Quit 
Output console
Running solution...

Compilation successful.

Example test:    [-1, 3, -4, 5, 1, -6, 2, 1] 
OK 

Your code is syntactically correct and works properly on the example test.
Note that the example tests are not part of your score. On submission at least 8 test cases not shown here will assess your solution.
accessibility mode is disabled