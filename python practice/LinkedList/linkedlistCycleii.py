# 142. Linked List Cycle II
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

'''
slow goes like: slow = slow.next
fast goes like: fast = fast.next.next
when they finally meet each other:
        let k be the distance from beginning to the beginning of the cycle
        let dFast be the total distance of fast
        let dSlow be the total distance of slow
        let c be the circumference of the cycle
        let m be the distance from the beginning of the cycle to the point where slow and fast meet each other
        let n be the number of cycles that fast goes through
        we have:
            dFast = 2 * dSlow
            dFast = k + m + n * c
            dSlow = k + m
        that is: k = n * c - m
        Therefore, if slow starts from head, and fast continue at where they met, and they are in same pace
            when slow reach the beginning of the cycle:
                dSlow = k = dFast
            bacause: k = n * c - m = (n - 1) * c + c - m  = dFast
        then we know fast goes through (n - 1) cycles and (c - m) distance then goes to the beginning of cycle as well.
'''


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None
