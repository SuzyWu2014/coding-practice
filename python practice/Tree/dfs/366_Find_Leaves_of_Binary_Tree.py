# 366. Find Leaves of Binary Tree

# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

# Example:
# Given binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Returns [4, 5, 3], [2], [1].

# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:

#           1
#          /
#         2
# 2. Now removing the leaf [2] would result in this tree:

#           1
# 3. Now removing the leaf [1] would result in the empty tree:

#           []
# Returns [4, 5, 3], [2], [1].


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        rst = []
        while root.left or root.right:
            rst.append(self.find_leaves(root))
        rst.append([root.val])
        return rst


    def find_leaves(self, root):
        stack = [root]
        leaves = []
        while stack:
            node = stack.pop()
            if node.left and node.left.left is None and node.left.right is None:
                leaves.append(node.left.val)
                node.left = None
            elif node.left:
                stack.append(node.left)

            if node.right and node.right.left is None and node.right.right is None:
                leaves.append(node.right.val)
                node.right = None
            elif node.right:
                stack.append(node.right)
        return leaves





