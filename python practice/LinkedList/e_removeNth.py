# 19. Remove Nth Node From End of list
# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

# 解题思路
# Nth from the end, 意思就是当一个指针走到最末的时候，另一个刚好跟他相差n,
# 也就是一快一慢两个指针，快的在前方N个节点处，然后两个节点一起往前走，
# 快指针到终点时，慢指针也就是到了我们要删除的节点。
# 但由于要删除，则需要前一个节点，引入dummy来解决问题
