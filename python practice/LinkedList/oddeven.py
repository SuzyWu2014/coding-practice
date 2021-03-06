# 328. Odd Even Linked List
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ..


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        odd = oddHead = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return oddHead

# 解题思路
# 像这种把list的值分成两个部分的，可以给两个部分各自一个dummy head
# 最后把左边的尾部练到右边的头部， 返回左边dummyhead.next
