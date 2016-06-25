# 234. Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        fast = slow = head
        # find the mid node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        p, last = slow.next, None
        while p:
            tmp = p.next
            p.next = last
            last = p
            p = tmp
        # check palindrome
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        # resume linked list
        # p, last = last, None
        # while p:
        #     tmp = p.next
        #     p.next = last
        #     last = p
        #     p = tmp
        # slow.next = last
        return p1 is None
