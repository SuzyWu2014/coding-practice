# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        inorder: left, root, right
        """
        if root is None:
            return True
        stack = []
        pre_node = None
        curr_node = root
        while stack or curr_node:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop() # most left node
                if pre_node:
                    if pre_node.val >= curr_node.val:
                        return False
                pre_node = curr_node
                curr_node = curr_node.right
        return True
