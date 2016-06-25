# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(0)
        while l1 or l2:
            if l1 is None:
                l3.next = l2
                break
            if l2 is None:
                l3.next = l1
                break
            if l1.val < l2.val:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
        return head.next
