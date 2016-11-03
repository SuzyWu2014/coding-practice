# You have n matrices, each with nxn entries (so you have n^3 numbers in total). For each matrix A, the entries are sorted:

# A_ij < A_ik for each row i and all columns j<k.

# A_ij < A_kj for each column j and all rows i<k.

# Design the fastest algorithm to select the n smallest numbers from these n^3 numbers.
import heapq

def n_smallest_nums(M):
    """
    :type M: List[List[List[a]]]
    :rtype: List[a]
    """
    heap = [(nums[0][0], a, 0, 0) for a, nums in enumerate(M)]
    heapq.heapify(heap)
    ele_set = set([(a, 0, 0) for a in xrange(len(M))])
    rst = []
    while len(rst) < len(M):
        val, a, i, j = heapq.heappop(heap)
        rst.append(val)
        if i + 1 < len(M[a]) and (a, i + 1, j) not in ele_set:
            ele_set.add((a, i + 1, j))
            heapq.heappush(heap, (M[a][i + 1][j], a, i + 1, j))
        if j + 1 < len(M[a][0]) and (a, i, j + 1) not in ele_set:
            ele_set.add((a, i, j + 1))
            heapq.heappush(heap, (M[a][i][j + 1], a, i, j + 1))
    return rst


if __name__ == '__main__':
    print( n_smallest_nums([]))
    print n_smallest_nums([[[1 , 5, 6],[2, 6, 7], [5, 7, 9]], [[3, 4, 6],[5, 7, 9], [6, 8, 10]], [[1,2,3],[4,5,6], [7, 8, 9]], [[2, 4, 5],[3, 6, 8], [4, 7, 9]]])
    print n_smallest_nums([[[1, 3, 6],[2, 6, 7], [5, 7, 9]], [[3, 4, 6],[5, 7, 9], [6, 8, 10]], [[1,2,3],[4,5,6], [7, 8, 9]], [[1, 4, 5],[2, 6, 8], [4, 7, 9]]])
