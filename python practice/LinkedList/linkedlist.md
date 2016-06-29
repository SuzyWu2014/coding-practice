# How to solve Linked List problems

## Be clear you are creating a new linked list or modify it in place.

## If you need to manipulate with 2 linked lists, think about what if they have different length.

+ tip 1: handle them separately,if one is None, just ignore it and handle the other one.

```python
while l1 or l2:
    if l1 is not None:
        # do something
        l1 = l1.next
    if l2 is not None:
        # do something
        l2 = l2.next
    # do something
    # or something when l1 and l2 both not None
```

+ tip 2: calculate their length difference, then start with the longer one first until he gets to the position where the remaining length is the same as the other one

```python
a, b = headA, headB  # faster than a = headA, b = headB
len_a, len_b = 0, 0
while a is not None:
    a = a.next
    len_a += 1
while b is not None:
    b = b.next
    len_b += 1
a, b = headA, headB
if len_a > len_b:
    for i in range(len_a - len_b):
        a = a.next
else:
    for i in range(len_b - len_a):
        b = b.next

# Now a and b are the same length to the end
```


## When your loop ends, check if there is something left need to be handled

## Check if two nodes are the same node, it's `if node1 == node2:` not `node1.val == node2.val`

## remove elements
    This usually needs a dummy head, and the current pointer always is the previous pointer of the one we want to remove

## Manipulate element positions
+ put the nodes into left or right group, think about a dummy head for left and right side, and connect tail of the left to the head of the right in the end.
+ 
