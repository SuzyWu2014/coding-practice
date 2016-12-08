# Final review

## 1 Give a real-life example of "changing" priorities
i.e., when do you need to call "decrease-key()" as in Dijkstra?

+ Emergency room: call decrease-key() when a patient's condition worsens.

## 2 Describe how to implement decrease-key().

```python
decrease-key(v, newkey):
    # look up heapdict and find the position of v, change the key to newkey
    # pop v in the heap using its newkey until it is larger than its father in heap
    # when swapping, update the position of two nodes in heapdict
```

## 3 For the following graphs, decide whether they are

(1) directed or undirected, and (2) dense or sparse:

   (a) Facebook: undirected, sparse
   (b) Twitter: directed, sparse
   (c) family: undirected, dense
   (d) airline map (V=airports, E=direct_flights): undirected, sparse
   (e) mesh: undirected, sparse

## 4. Give two real-life examples of topological sort.

+ dressing up
+ cooking
+ taking courses w.r.t. prerequisites

## 5. Tipological sort

We covered BFS implementation of topological sort,
   and the topological order is used in bottom-up approaches in DP (Viterbi).
   How to use DFS for topological sort?
   How does it connect to the top-down approach in DP?

## 6. Can Dijkstra work for all DAGs? Give example(s).

No, only works with non-negative weights

## 7. What's the time complexity of Dijkstra if you use the following implementations of priority queue?

### binary heap

`O((V + E) log v)`

### unsorted array

+ `O(V)` to extract min
+ `O(1)` to decrease key

`O(V^2 + E) => O(v^2)`

### sorted array

+ Traditional
    * `O(v)` to extract first element from the sorted list
    * `O(v)` to decrease key and move it to a right position
    * `O(V^2 + EV)`

+ Use decrease-key on all candicate edges together for a vertex:
    * `O(V)` to extract first element from the sorted list
    * `O(1)` to decrease-key
    * `O(vlogv)` to sort the list
    * `O(V^2 + E + V^2 log V) = O(V^2 log V)`

### Fibonacci heap (not taught in class, but covered in CLRS)

+ `O(log V)` to extract min
+ `O(1)` to decrease-key
+ `O(vlog V + E)`

## 8. Dijkstra with integer weights:

suppose all edge weights are in {1..W} where W is a positive integer but not a const. Modify priority queue datastructure to achieve O(VW+E) time. (hint: no heap).

[ranged-weight-dijkstra.py](ranged-weight-dijkstra.py)

## 9. Weird shortest path:

find the path whose longest edge is the shortest.motivation: My car has a small tank, and gas stations are only found in cities.

## 10. Draw the hypergraph for: (neglect the edges and just draw the hyperedges)

   (a) best() for ACGU.
       list at least three topological orders.

   (b) number of binary search trees of 3 nodes.
       how many topological orders can you get?

## 11. Fill-in-the-blanks question:  [NO Fill-in-the-blanks in Final! But there will be problmes similar to these]

Variant of one of the following:
TSP (three versions), RNA best(), RNA total(),
Viterbi (including topological sort), or Dijkstra.

## 12. Given a boolean expression, count the number of parenthesizations that return T.
   e.g.,

   input: F + F * T    output: 0. reason: impossible
   input: T + F * T    output: 2. reason: (T+(F*T))   ((T+F)*T)

   O(n^3) or better.

[count_true.py](count_true.py)

## 13. Each integer can be represented as the sum of squares,
e.g.:
   1 = 1*1      (partition size 1)
   2 = 1*1 + 1*1    (partition size 2)
   4 = 2*2          (partition size 1)
   5 = 2*2 + 1*1    (partition size 2)

   For a given integer N, find the smallest partition (e.g., for N=4, return 1; for N=5, return 2).

   O(n^2) or better.

[smallest_partition.py](smallest_partition.py)

## 14. How to get k-best shortest path using Viterbi?

[kbest-shortest-path.py](kbest-shortest-path.py)

## 15. For single-source single-sink shortest paths on DAGs with non-negative weights, which one is faster, Dijkstra or Viterbi?

### Dijkstra VS Viterbi

|               |   Dijkstra    |   Viterbi     |
| ------------- |:-------------:| -------------:|
|Time complexity| `O((V + E)log V)`|   `O(V + E)`   |

Viterbi is faster; However, Dijkstra stops when the sink-node is popped out. In practical, the time spent would depend on the rank of the sink among all the vertices in terms of distance from source vertex.

## Convert DP problem to Dijkstra/viterbi

A vertex indicates a sub-problem, edges indicate the relationship of a parent-problem and its sub-problems.

### Graph-structured DP problems

#### TSP

The idea is to convert TSP problem into hypergragh. Each vertex indicates (visited_set, dest_city), each edges indicates a distance from a visited set to another.

`([0, 1], 1) --w(1, 2)--> ([0,1,2], 2)`

For instance,

|||
|:-------------:| -------------:|
|   **Dijkstra** |source vertex: ([0], 0); sink vertex: ([0, 1...v], x) x from 1 to v. Find the shortest path from source to sink.|
|   **Viterbi**  |Find the shortest path from source to sink based on topological sort|

### Only Viterbi

All convert to longest path problem.

#### LIS

Each letter is represented as a vertex, and an edge from a to b when there is an increase from letter 'a' to letter 'b'.

#### Knapsacks

#### MIS

Each element in the list is represented as a vertex, and an edge `a -> b` when `a`and `b` can be in the independent set.
The weight is the value of the element.

### Only Dijkstra

Road network problem, since the graph is undirected.





