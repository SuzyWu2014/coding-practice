# -*- coding: utf-8 -*-
# 230. Kth Smallest Element in a BST
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Hint:
# BST具有如下性质：

# 左子树中所有元素的值均小于根节点的值

# 右子树中所有元素的值均大于根节点的值

# 因此采用中序遍历（左 -> 根 -> 右）即可以递增顺序访问BST中的节点，从而得到第k小的元素，时间复杂度O(k)


# Try to utilize the property of a BST.
# What if you could modify the BST node's structure?
# The optimal runtime complexity is O(height of BST).


class TreeNode(object):
    def __init__(self, x, y):
        self.val = x
        self.left = None
        self.right = None
        self.left_count = y


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while stack and x <= k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val

    def kthSmallest2(self, root, k):
        node = root
        if k == node.left_count + 1:
            return node
        elif k > node.left_count:
            k -= node.left_count + 1
            node = node.right
            return self.kthSmallest2(node, k)
        else:
            node = node.left
            self.kthSmallest2(node, k)
