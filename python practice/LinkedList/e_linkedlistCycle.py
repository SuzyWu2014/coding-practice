# 141. Linked List Cycle
# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 解题思路
# 快指针与慢指针
# 两者相遇，则说明有cycle
