"""-*- coding: utf-8 -*-"""
import mylist

"""206. Reverse a singly linked list."""


class Solution(object):
    def reverseList_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :Algorithm:
           - Interate through the list
           - maintain a pointer indicating the next node
           - maintain a previous node, starting from None
           - make current node point to previous node
           - make previous node goes to current node
           - make current node point to next node
        """
        curr = head
        prev = None

        while (curr is not None):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev

    def reverseList_recursive(self, head):
        """
          :type head: ListNode
          :rtype: ListNode
          :Algorithm:
             - devide list into head + headnext
             - reverse headnext bu recursive call
             - combine with head
               - headnext.next -> head
               - head.next -> Node
          """
        if head is None or head.next is None:
            return head
        rst = self.reverseList_recursive(head.next)
        head.next.next = head
        head = None
        return rst


nodes = mylist.createList([1, 2, 3, 4])
mylist.showList(nodes)
mylist.showList(Solution().reverseList_iterative(nodes))
