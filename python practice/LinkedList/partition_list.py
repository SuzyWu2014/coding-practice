# 86. Partition List
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
import mylist


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        left_dummy = mylist.ListNode(0)
        right_dummy = mylist.ListNode(0)
        left = left_dummy
        right = right_dummy
        while head:
            if head.val >= x:
                right.next = head
                right = head
            else:
                left.next = head
                left = head
            head = head.next
        left.next = right_dummy.next
        right.next = None
        return left_dummy.next


nodes = mylist.createList([4, 3])
mylist.showList(nodes)
mylist.showList(Solution().partition(nodes, 4))
nodes = mylist.createList([1, 5, 4])
mylist.showList(nodes)
mylist.showList(Solution().partition(nodes, 3))
nodes = mylist.createList([4, 2, 1, 3])
mylist.showList(nodes)
mylist.showList(Solution().partition(nodes, 3))

# 解题思路

