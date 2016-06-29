# 160. Intersection of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB  # faster than a = headA, b = headB
        len_a, len_b = 0, 0
        while a is not None:
            a = a.next
            len_a += 1
        while b is not None:
            b = b.next
            len_b += 1
        a, b = headA, headB
        if len_a > len_b:
            for i in range(len_a - len_b):
                a = a.next
        else:
            for i in range(len_b - len_a):
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a


# 解题思路：
# 题目是要返回intersection node，
# intersection node 的特点就是两个linked list 的某个节点同时指向了这个node,
# 问题在于两个list的长度不同的情况下，他们无法同时到达这个相交点
# 这边的技巧就是找到长度的差值，然后使长的liinked list 先走一段
