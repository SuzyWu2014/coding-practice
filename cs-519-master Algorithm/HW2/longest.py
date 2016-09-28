def longest(tree):
    if tree is None or len(tree) == 0:
        return 0
    path, depth = _longest(tree)
    return path - 1


def _longest(tree):
    if tree == []:
        return 0, 0
    l_path, l_depth = _longest(tree[0])
    r_path, r_depth = _longest(tree[2])
    return max(l_depth + r_depth + 1, l_path, r_path), max(l_depth, r_depth) + 1
