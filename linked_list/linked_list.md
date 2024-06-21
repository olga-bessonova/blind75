# Linked List 
A linked list is a collection of nodes where each node contains data as well as the memory address of the next node in the list.

https://www.freecodecamp.org/news/introduction-to-linked-lists-in-python/
https://www.freecodecamp.org/news/how-linked-lists-work/

## Advantages of Linked Lists:
1. Because of the chain-like system of linked lists, you can add and remove elements quickly. 
 This also doesn't require reorganizing the data structure unlike arrays or lists. Linear data structures are often easier to implement using linked lists.
2. Linked lists also don't require a fixed size or initial size due to their chainlike structure.

## Disadvantages of a Linked Lists:
1. More memory is required when compared to an array. This is because you need a pointer (which takes up its own memory) to point you to the next element.
2. Search operations on a linked list are very slow. Unlike an array, you don't have the option of random access.

| List Type         | Description                                                                                          | Directionality                        |
|-------------------|------------------------------------------------------------------------------------------------------|---------------------------------------|
| Singly Linked     | Nodes have a single pointer connecting them in a single direction.                                   | Head→Tail                             |
| Doubly Linked     | Nodes have two pointers connecting them bi-directionally.                                            | Head⇄Tail                             |
| Multiply Linked   | Nodes have two or more pointers, providing a variety of potential node orderings.                    | Head⇄Tail, A→Z, Jan→Dec, etc.         |
| Circularly Linked | Final node's next pointer points to the first node, creating a non-linear, circular version of a Linked List. | Head→Tail→Head→Tail                  |
  |


## Time and Space complexity
** Space complexity for both types of linked lists is O(n), as each element requires space for its data and pointers to the next (and possibly previous) node, resulting in linear space usage proportional to the number of elements.

| Data Structure Operation | Time Complexity (Avg) | Time Complexity (Worst) | Space Complexity (Worst) |
|--------------------------|-----------------------|--------------------------|--------------------------|
| Access                   | Θ(n)                  | O(n)                     | O(n)                     |
| Search                   | Θ(n)                  | O(n)                     | O(n)                     |
| Insertion                | Θ(1)                  | O(1)                     | O(n)                     |
| Deletion                 | Θ(1)                  | O(1)                     | O(n)                     |                      |

## When Should You Use a Linked List?
You should use a linked list over an array when:

You don't know how many items will be in the list (that is one of the advantages - ease of adding items).
You don't need random access to any elements (unlike an array, you cannot access an element at a particular index in a linked list).
You want to be able to insert items in the middle of the list.
You need constant time insertion/deletion from the list (unlike an array, you don't have to shift every other item in the list first).