# AVL Tree: Find the k-th Smallest Element

This project demonstrates how to find the **k-th smallest element** in an AVL tree (a self-balancing Binary Search Tree), using an **in-order traversal** technique.

## Approach

The solution uses two methods:

1. **In-order Traversal:**
   - Traverse the tree recursively, visiting nodes in **left → root → right** order.
   - Append each node's value to a list.

2. **Find k-th Smallest:**
   - After performing the in-order traversal, the list of nodes will be in sorted order.
   - Simply return the element at the index `k-1`, where `k` is the desired smallest element.

---

## Code Explanation

- `inorder_traversal(node, smallest_elements)`: Recursively traverses the tree and appends node values to `smallest_elements`.
- `smallest_kth_element(k)`: After collecting all node values in sorted order, returns the `k`-th smallest element by index `k-1`.

---

## 🧪 Example

Given this tree:
      50
     /  \
   30    70
  / \    / \
20  40  60  80

The **in-order traversal** will result in the following sorted list of values:
[20, 30, 40, 50, 60, 70, 80]

- The **1st smallest element** is `20`
- The **4th smallest element** is `50`
- The **7th smallest element** is `80`
