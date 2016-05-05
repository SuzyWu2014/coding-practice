"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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


node_1 = ListNode('1')
node_2 = ListNode('2')
node_3 = ListNode('3')
node_4 = ListNode('4')
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
l=node_1
print l.val +" "+ l.next.val + " " +l.next.next.val +" "+ l.next.next.next.val 
l = Solution().reverseList_iterative(node_1)
print l.val +" "+ l.next.val + " " +l.next.next.val +" "+ l.next.next.next.val 
l = Solution().reverseList_recursive(l)
print l.val +" "+ l.next.val + " " +l.next.next.val +" "+ l.next.next.next.val 


