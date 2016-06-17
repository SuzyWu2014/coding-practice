# 92. Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.

import mylist


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is not None or head.next is not None:
            return head
        dummy = mylist.ListNode(0)
        dummy.next = head
        head1 = dummy
        for i in range(m - 1):
            head1 = head1.next
        p = head1.next
        for i in range(n - m):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next
        # if m == n:
        #     return head
        # dummy = mylist.ListNode(0)
        # dummy.next = head
        # before_reverve = dummy
        # for i in range(m - 1):
        #     before_reverve = before_reverve.next
        # reverse_head = before_reverve.next
        # for i in range(n - m):
        #     tmp = before_reverve.next
        #     before_reverve.next = reverse_head.next
        #     before_reverve.next.next = tmp
        #     reverse_head.next = reverse_head.next.next
        # return dummy.next


nodes = mylist.createList([1, 2, 3, 4, 5, 6])
mylist.showList(nodes)
mylist.showList(Solution().reverseBetween(nodes, 3, 6))
mylist.showList(Solution().reverseBetween(nodes, 3, 5))
mylist.showList(Solution().reverseBetween(nodes, 1, 6))
