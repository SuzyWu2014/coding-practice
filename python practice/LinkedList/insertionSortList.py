# 147. Insertion Sort List
# Sort a linked list using insertion sort.


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next

# 解题思路
# insertion sort:
# 3 2 1 4 5
# 2 3 1 4 5
# 1 2 3 4 5
# 当前指针的值从头开始对比，一旦发现比他小的值，则插入
# 为了简化插入位置为head之前的情况，引入dummy head
