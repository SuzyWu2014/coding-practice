# 143. Reorder List
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
import mylist


class Solution(object):

    def get_median(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = slow.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        dummy = mylist.ListNode(0)
        dummy.next = head
        curr = head.next
        head.next = None
        while curr:
            pre_head = dummy.next
            dummy.next = curr
            next_node = curr.next
            curr.next = pre_head
            curr = next_node

        return dummy.next

    def combineTwo(self, left, right):
        dummy = mylist.ListNode(0)
        curr = dummy
        while left and right:
            tmp_next_left = left.next
            tmp_next_right = right.next
            curr.next = left
            curr.next.next = right
            left = tmp_next_left
            right = tmp_next_right
            curr = curr.next.next
        return dummy.next

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if (head is None) or (head.next is None) or (head.next.next is None):
            return
        mid = self.get_median(head)
        snd_half = mid.next
        mid.next = None
        reversed_snd_half = self.reverse(snd_half)
        head = self.combineTwo(head, reversed_snd_half)


nodes = mylist.createList([1])
mylist.showList(nodes)
mylist.showList(Solution().reorderList(nodes))
nodes = mylist.createList([1, 5, 4])
mylist.showList(nodes)
mylist.showList(Solution().reorderList(nodes))
nodes = mylist.createList([1, 2, 3, 4, 5, 6])
mylist.showList(nodes)
mylist.showList(Solution().reorderList(nodes))

# 解题思路：
# 找到中点
# 反转右边
# 连接左右两边
