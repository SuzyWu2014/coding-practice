# 82. Remove Duplicates from Sorted List II
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

import mylist


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = mylist.ListNode(0)
        dummy.next = head
        p = dummy
        tmp = dummy.next
        while p.next:
            while tmp.next and tmp.next.val == p.next.val:
                tmp = tmp.next
            if tmp == p.next:
                p = p.next
                tmp = p.next
            else:
                p.next = tmp.next
        return dummy.next


nodes = mylist.createList([1, 1, 1, 3, 4, 4])
mylist.showList(nodes)
mylist.showList(Solution().deleteDuplicates(nodes))
nodes = mylist.createList([1, 3])
mylist.showList(nodes)
mylist.showList(Solution().deleteDuplicates(nodes))

# 解题思路：
# 慢指针停在我们要保留的节点上，
# 然后通过比较慢指针的下一个节点以及 随后的节点，知道找到不相同的
# 注意点，就是没有重复节点的判定，也就是慢指针的随后两个节点都不一样
