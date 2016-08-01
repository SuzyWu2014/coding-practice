# 199. Binary Tree Right Side View
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                top = queue.pop(0)
                if i == 0:
                    res.append(top.val)
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append((top.left))
        return res

# 解题思路：
# 将每一层的node从右往左放入queue
# 每次取第一个放入res, 其余将下一层节点放入queue
