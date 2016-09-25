#!/usr/bin/env python


def qsort(nums):
    """Buggy version of quicksort"""
    if len(nums) == 0:
        return []
    pivot = nums[0]
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]
    left = qsort(left)
    right = qsort(right)
    return [left] + [pivot] + [right]


def pp(tree, level=0):
    if tree == []:
        return
    left, root, right = tree
    print("|" * level + str(root))
    pp(left, level + 1)
    pp(right, level + 1)


def sorted(t):
    """
    Returns the sorted order(infix traversal) - left-root-right
    """
    if not t:
        return []
    left, root, right = t
    return sorted(left) + [root] + sorted(right)


def search(t, x):
    """
    returns whether x is in t
    """
    if not t:
        return False
    left, root, right = t
    return search(left, x) or root == x or search(right, x)


def insert(t, x):
    """
    inserts x into t (in-place) if it is missing, otherwise does nothing.
    """
    if not t:
        return [[], x, []]
    left, root, right = t
    if x < root:
        return [insert(left, x), root, right]
    elif x > root:
        return [left, root, insert(right, x)]
    else:
        return t

tree = qsort([4,2,6,3,5,7,1,9])
pp(tree)
tree = insert(tree, 6.5)
print tree
pp(tree)