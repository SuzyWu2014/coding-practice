# 83. Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

import mylist


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        curr = head
        while curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

nodes = mylist.createList([1, 1, 1, 3, 4, 4])
mylist.showList(nodes)
mylist.showList(Solution().deleteDuplicates(nodes))
nodes = mylist.createList([1, 3])
mylist.showList(nodes)
mylist.showList(Solution().deleteDuplicates(nodes))

# 解题思路：
# 要删除sorted list里的重复值，只需要对比相邻的节点，
# curr 指针就留在当前会保留的最后的一个元素上
# 要删除的永远是curr指针的下一个元素，故而需要前置指针的信息
