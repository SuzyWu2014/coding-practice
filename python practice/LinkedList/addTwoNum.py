# 2. Add Two Numbers
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = head = ListNode(0)
        carry = 0
        while l1 or l2:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            l3.next = ListNode(carry % 10)
            carry = carry / 10
            l3 = l3.next
        if carry == 1:
            l3.next = ListNode(1)
        return head.next

# 解题思路：
# 题目要求将和作为新的Linked List返回，故而将需要一个新的head, 每计算一位，就新建一个新的node.
# 需要注意的是两个整数不一定有同样的位数，也就是说会出现一个list 已经结束，但是另一个还在中间。以及最后要检查是否有进位。
# 技巧就是要重复使用carry变量， 分别将两个数加至carry 上，若List已经到头，则无需加。
