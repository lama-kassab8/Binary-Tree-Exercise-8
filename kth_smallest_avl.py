class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

class AVL:
    def __init__(self):
        self.root= None

    def inorder_traversal(self, node, smallest_elements):
        if node:
            self.inorder_traversal(node.left, smallest_elements) # visit the left subtree first
            smallest_elements.append(node.data) # append the current node to the list
            self.inorder_traversal(node.right, smallest_elements) # visit the right subtree

    def smallest_kth_element(self, k):
        smallest_elements= []
        self.inorder_traversal(self.root, smallest_elements)
        # check if k is within valid range:
        # k must be at least 1, then k-1 will be invalid index
        # k must not exceed the number of elements in the tree
        # if k satisfies both checks, return the smallest element which is accessed by index k-1
        if 1 <= k <= len(smallest_elements): 
            return smallest_elements[k-1] # because lists are zero-indexed, k will be at index k-1
        else:
            return None
        
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

avl= AVL()
avl.root= root
# Run the test
print("Smallest element:", avl.smallest_kth_element(4))
