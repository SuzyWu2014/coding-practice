# 148. Sort list
# Sort a linked list in O(n log n) time using constant space complexity.
import mylist


class Solution(object):

    def get_median(self, head):
        slow = head
        fast = head.next
        # get mid
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid = self.get_median(head)
        right = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(right)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy_head = mylist.ListNode(0)
        curr = dummy_head
        while left is not None and right is not None:
            if left.val > right.val:
                curr.next = right
                curr = curr.next
                right = right.next
            else:
                curr.next = left
                left = left.next
                curr = curr.next
        if left is None:
            curr.next = right
        if right is None:
            curr.next = left
        return dummy_head.next


nodes = mylist.createList([4, 3])
mylist.showList(nodes)
mylist.showList(Solution().sortList(nodes))
nodes = mylist.createList([1, 5, 4])
mylist.showList(nodes)
mylist.showList(Solution().sortList(nodes))
nodes = mylist.createList([4, 2, 1, 3])
mylist.showList(nodes)
mylist.showList(Solution().sortList(nodes))
