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

# 解题思路：
# 需要注意的问题1，两个list长度不同，可分别处理当其中一个已经为None的情况，再来处理都不为None的情况
# in place 修改的情况，通常加一个dummy head 会比较有帮助，一颗减少需要额外处理head的情况
# 本题并不需要交换node,所以并不需要记录前置节点
