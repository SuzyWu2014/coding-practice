# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next

node_1 = ListNode('1')
node_2 = ListNode('2')
node_3 = ListNode('3')
node_4 = ListNode('4')
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
l = node_1
print l.val + " " + l.next.val + " " + l.next.next.val + " " + l.next.next.next.val
l = Solution().swapPairs(node_1)
print l.val + " " + l.next.val + " " + l.next.next.val + " " + l.next.next.next.val
