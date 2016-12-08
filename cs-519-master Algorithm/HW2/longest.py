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


def _track_longest(tree):
    if tree == []:
        return [], []
    l_path, l_depth = _track_longest(tree[0])
    r_path, r_depth = _track_longest(tree[2])
    longest_path = max(len(l_path), len(r_path), len(l_depth) + len(r_depth) + 1)
    depth = l_depth + [tree[1]] if len(l_depth) > len(r_depth) else [tree[1]] + r_depth
    if longest_path == len(l_path):
        return l_path, depth
    elif longest_path == len(r_path):
        return r_path, depth
    else:
        return l_depth + [tree[1]] + r_depth, depth
