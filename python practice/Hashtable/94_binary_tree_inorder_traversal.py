# 94. Binary Tree Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res

    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal2(root.left)
            self.result.append(root.val)
            self.inorderTraversal2(root.right)
        return self.result
