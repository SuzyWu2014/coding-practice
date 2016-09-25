#!/usr/bin/env python


def sort(nums):
    """Buggy version of quicksort"""
    if nums is None or len(nums) == 0:
        return []
    pivot = nums[0]
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]
    left = sort(left)
    right = sort(right)
    return [left] + [pivot] + [right]


def pp(tree, level=0):
    if tree is None or tree == []:
        return
    left, root, right = tree
    print("|" * level + str(root))
    pp(left, level + 1)
    pp(right, level + 1)


def sorted(t):
    """
    Returns the sorted order(infix traversal) - left-root-right
    """
    if t is None or t == []:
        return []
    left, root, right = t
    return sorted(left) + [root] + sorted(right)

def search(t, x):
    """
    Returns whether x is in t
    """
    if t is None or t == []:
        return False
    return len(_search(t, x)) > 0


def insert(t, x):
    """
    inserts x into t (in-place) if it is missing, otherwise does nothing.
    """
    if t is None:
        t = [[], x, []]
        pass
    subtree = _search(t, x)
    if subtree == []:
        subtree.extend([[], x, []])


def _search(t, x):
    """
    Returns the subtree (a list) rooted at x when x is found,
        or the [] where x should be inserted.
    """
    if t == [] or x == t[1]:
        return t
    elif x < t[1]:
        return _search(t[0], x)
    else:
        return _search(t[2], x)


# Solution 1: without helper function
def search_1(t, x):
    """
    Returns whether x is in t
    """
    if t is None or t == []:
        return False
    left, root, right = t
    return search(left, x) or root == x or search(right, x)


def insert_sol1(t, x):
    """
    inserts x into t if it is missing, otherwise does nothing. => not in-place
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
