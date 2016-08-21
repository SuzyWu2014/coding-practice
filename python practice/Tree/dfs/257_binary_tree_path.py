# 257. Binary Tree Paths
# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        result = []
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, tmp):
        tmp.append(str(node.val))
        if node.left is None and node.right is None:
            result.append('->'.join(tmp))
            tmp.pop()
            return

        if node.left:
            self.dfs(node.left, result, tmp)
        if node.right:
            self.dfs(node.right, result, tmp)
        tmp.pop()
