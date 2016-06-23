# 61. Rotate List
# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow = fast = head
        length = 0
        while fast is not None:
            fast = fast.next
            length += 1
        k = k % length
        if k == 0:
            return head
        fast = head
        for i in range(k):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        tmp = slow.next
        slow.next = None
        fast.next = head
        return tmp
