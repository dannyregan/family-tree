# """
# node class
# in order traversion class
# make this tree in the main
# tell him the order it prints out
# """

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# # def inOrderTraversal(root):
# #     if root:
# #         inOrderTraversal(root.left)
# #         print(root.data)
# #         inOrderTraversal(root.right)
        
# # def main():
# #     root = Node(1)
# #     root.left = Node(6)
# #     root.right = Node(3)
# #     root.left.left = Node(4)
# #     root.left.right = Node(2)
# #     root.right.left = Node(5)
# #     root.right.right = Node(7)
# #     inOrderTraversal(root)

# def insert(root, key):
#     if root is None:
#         return Node(key)
#     if key < root.data:
#         root.left = insert(root.left, key)
#     else:
#         root.right = insert(root.right, key)
#     return root

# def search(root, key):
#     if root is None or root.data == key:
#         return root
#     if key < root.data:
#         return search(root.left, key)
#     else:
#         return search(root.right, key)
    
# def main():
#     root = Node(50)
#     root = insert(root, 70)
#     root = insert(root, 30)
#     result = search(root, 70)

#     if result:
#         print(result.data)

# main()


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def insert(root, key, side):
    if root is None:
        return Node(key)
    if side == 'L':
        root.left = insert(root.left, key, side)
    else:
        root.right = insert(root.right, key, side)
    return root
    
def print_tree(root, indent="", last=True):
    """ Prints the tree in a structured, indented format. """
    if root:
        print(indent, end="")
        if last:
            print("R----", end="")
            indent += "     "
        else:
            print("L----", end="")
            indent += "|    "

        print(root.name)

        if root.left or root.right:
            print_tree(root.left, indent, False)
            print_tree(root.right, indent, True)

class App:
    def __init__(self):
        self.root = None
        self.creatures = []

    def add_root_creature(self, name):
        self.root = Node(name)
        self.creatures.append(self.root)

    def add_creature(self, parent_name, child_name, side):
        parent_node = self.search(self.root, parent_name)
        if parent_node:
            insert(parent_node, child_name, side)
            print(f"{child_name.upper()} has been added to the tree as {side} child of {parent_name}.")
        else:
            print("That parent creature does not exist.")

    def search(self, root, key):
        if root is None or root.name == key:
            return root
        left_search = self.search(root.left, key)
        if left_search is not None:
            return left_search
        return self.search(root.right, key)

    def print_specific(self, creature_name):
        if not self.root:
            print("No creatures in the tree.")
            return
        print(f"Ancestors of {creature_name}:")
        if not print_ancestors(self.root, creature_name):
            print(f"{creature_name} does not exist in the tree.")

    def print_all(self):
        if self.root:
            print("Tree structure:")
            print_tree(self.root)
        else:
            print("No creatures in the tree.")

def menu():
    app = App()

    while True:
        print()
        print('======= Menu =======')
        print('1) Add Root Creature')
        print('2) Add Creature')
        print('3) Print All')
        print('4) Print Specific Creature Ancestors')
        print('0) Exit')
        print('====================')
        selection = input('Choose an option: ')

        if selection == '1':
            name = input("What's the root creature's name? ")
            app.add_root_creature(name)

        elif selection == '2':
            parent = input("What's the parent's name? ")
            name = input("What's the creature's name? ")
            side = input("Input L or R child: ").upper()
            if side in ['L', 'R']:
                app.add_creature(parent, name, side)
            else:
                print("Invalid side input. Use 'L' or 'R'.")

        elif selection == '3':
            app.print_all()

        elif selection == '4':
            creature = input("Enter the creature's name: ")
            app.print_specific(creature)

        elif selection == '0':
            break
        else:
            print("Invalid input.")

# =================================================
menu()
