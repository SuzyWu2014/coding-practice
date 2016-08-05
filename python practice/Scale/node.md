## Imagine you have data being pulled very frequently from a large database. How would you design a MRU (most recently used) cache?

data structure:
+ id
+ value
+ timestamp

hash map to store the data, if hit value, update the timestamp, add it to map,


## Design and implement an algorithm to merge N sorted arrays.
1. Take the head of all the N sorted arrays in a min-heap.
2. Get the min element from the min-heap and output/store it.
3. now pull out another element from the array to which the min-element in 2. belonged and add it to the heap and heapify it.
4. now repeat 2. & 3. till all the elements in N sorted arrays are exhausted.

## How would you write a benchmark to calculate the time of each memory access?
http://www.mcs.anl.gov/~kazutomo/hugepage/

Memory access pattern

+ Stream copy access pattern

The first pattern is a simple memory copy like pattern, which simply divides an allocated memory region half and copy from a half to another half element by element. This type of memory access pattern obvious shows characteristic of hardware prefetch.

+ random copy access pattern

The second pattern picks randomly two positions, loads data from the first position and saves it to the second position. This access pattern may show TLB miss penalty.

+ random read access pattern

The last one does only load operation while previous two pattens are load, store combination. Each element in the memory array contains a random number which is less than the size of array. The content of element is going to be an index for the next load operation.


