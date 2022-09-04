# General Notes

## Data structure

- There are only two ways to store data structure: array (sequential storage) and linked list (linked storage)。
- All _hash table, stack, queue, heap, tree, graph and etc_ are doing special operations on linked lists or arrays, just have different APIs
- The advantages and disadvantages of the two are as follows:

  - **Array** is continuous storage, which can be accessed **randomly**. It can find corresponding elements quickly through index and save storage space relatively. But just because of the continuous storage, the memory space must be allocated enough at one time, so if the array is to be expanded, it needs to reallocate a larger space, and then copy all the data, the time complexity O (n); and if you want to insert and delete in the middle of the array, you must move all the data behind each time to maintain the continuity, the time complexity O (n).

  - Because the elements of the **linked list** are not continuous, but the pointer points to the position of the next element, so there is no expansion of the array; if you know the precursor and the hind drive of an element, the operation pointer can delete the element or insert a new element, with time complexity of O (1). But because the storage space is not continuous, **you can't calculate the address of the corresponding element according to an index, so you can't access it randomly**; and because each element must store a pointer to the location of the front and back elements, it will consume relatively more storage space.

## Basic operation of data structure

Traversal and access of various data structures are in two forms: **linear** and **nonlinear**. Linear is represented by for / while iteration, and nonlinear is represented by recursion. Furthermore, there are only the following frameworks:

- Array traversal, typical linear iterative structure：

```python
for element in elements:
    ...

for i, element in enumerate(elements, 0):
    ...
```

- Linked list traversal has both iterative and recursive structure：

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


cur = head
while cur {
    // iteratively cur.val
    cur = cur.next
}

def traverse(head: ListNode):
     // recursively head.val
     traverse(head.next)
```

- Binary tree traversal, typical nonlinear recursive traversal structure：

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traverse(root: TreeNode ):
    traverse(root.left)
    traverse(root.right)

```

- The binary tree can be extended to the n-tree traversal framework：

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children: List[TreeNode] = []

def traverse(root: TreeNode ):
    for child in root.children:
        traverse(child)

```

- **_Do binary tree exercises first_**, almost all the topics of binary trees are a set of this framework

```python
def traverse(root: TreeNode):
    # pre order traverse
    traverse(root.left)
    # middle order traverse
    traverse(root.right)
    # post order traverse
```
