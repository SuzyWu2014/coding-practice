# Final review

## 14. How to get k-best shortest path using Viterbi?

Vertex: 

## 15. For single-source single-sink shortest paths on DAGs with non-negative weights, which one is faster, Dijkstra or Viterbi?

### Dijkstra VS Viterbi

|               |   Dijkstra    |   Viterbi     |
| ------------- |:-------------:| -------------:|
|Time complexity| `O((V + E)log V)`|   `O(V + E)`   |

Viterbi is faster; However, Dijkstra stops when the sink-node is poped out. In pratical, the time spent would depend on the rank of the sink among all the vertices in iterms of distance from source vertices.

## Convert DP problem to Dijkstra/viterbi

Vertex indicates a sub-problem, edges indicate the relationship of a parent-problem and its sub-problems.

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





