class ListNode(object):
    """ Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


def createList(nums):
    head = ListNode(0)
    curr = head
    for num in nums:
        node = ListNode(num)
        curr.next = node
        curr = curr.next
    return head.next


def showList(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print("\n")
