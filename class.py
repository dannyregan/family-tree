"""
node class
in order traversion class
make this tree in the main
tell him the order it prints out
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def inOrderTraversal(root):
#     if root:
#         inOrderTraversal(root.left)
#         print(root.data)
#         inOrderTraversal(root.right)
        
# def main():
#     root = Node(1)
#     root.left = Node(6)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(2)
#     root.right.left = Node(5)
#     root.right.right = Node(7)
#     inOrderTraversal(root)

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
def main():
    root = Node(50)
    root = insert(root, 70)
    root = insert(root, 30)
    result = search(root, 70)

    if result:
        print(result.data)

main()