# -*- coding: utf-8 -*-
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
        if m == n:
            return head
        dummy = mylist.ListNode(0)
        dummy.next = head
        before_reverve = dummy
        for i in range(m - 1):
            before_reverve = before_reverve.next
        reverse_head = before_reverve.next
        for i in range(n - m):
            tmp = before_reverve.next
            before_reverve.next = reverse_head.next
            reverse_head.next = reverse_head.next.next
            before_reverve.next.next = tmp
        return dummy.next

    def reverseBetween2(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = mylist.ListNode(0)
        dummy.next = head
        start_rvs = dummy
        for i in range(m - 1):
            start_rvs = start_rvs.next
        end_rvs = start_rvs.next
        curr = start_rvs.next.next
        for i in range(n - m):
            tmp = curr.next
            curr.next = start_rvs.next
            start_rvs.next = curr
            curr = tmp
        end_rvs.next = curr
        return dummy.next


nodes = mylist.createList([1, 2, 3, 4, 5, 6])
mylist.showList(nodes)
mylist.showList(Solution().reverseBetween2(nodes, 3, 6))
mylist.showList(Solution().reverseBetween2(nodes, 3, 5))
mylist.showList(Solution().reverseBetween2(nodes, 1, 6))
nodes = mylist.createList([1, 2])
mylist.showList(nodes)
mylist.showList(Solution().reverseBetween2(nodes, 1, 2))

# 解题思路
# 节点交换时：
# 先保存 curr的下一个位置
# curr.next = something
# something =
# curr = tmp
