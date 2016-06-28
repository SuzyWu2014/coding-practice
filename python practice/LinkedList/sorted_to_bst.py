# 109. Convert Sorted List to Binary Search Tree
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


class TreeNode(object):
    '''definition for a binary tree node.'''

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sorted_array = []
        curr = head
        while curr:
            sorted_array.append(curr.val)
            curr = curr.next
        return self.sortedArrayToBST(sorted_array)

    def sortedArrayToBST(self, sorted_array):
        length = len(sorted_array)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(sorted_array[0])
        root = TreeNode(sorted_array[length / 2])
        root.left = self.sortedArrayToBST(sorted_array[:length / 2])
        root.right = self.sortedArrayToBST(sorted_array[length / 2 + 1:])
        return root
