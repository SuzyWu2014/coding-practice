# 173. Binary Search Tree Iterator
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.


class TreeNode(object):
    """ Definition for a  binary tree node"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.minval = 0
        self.left = []
        while root is not None:
            self.left.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.left) == 0:
            return False
        else:
            currNode = self.left.pop()
            self.minval = currNode.val

            if currNode.right is not None:
                newNode = currNode.right
                while newNode is not None:
                    self.left.append(newNode)
                    newNode = newNode.left
            return True

    def next(self):
        """
        :rtype: int
        """
        return self.minval

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())