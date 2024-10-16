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

def print_tree(root, indent="", right=True):
    if root:
        print(indent, end="")
        if right:
            print("R--", end="")
            indent += "    "
        else:
            print("L--", end="")
            indent += "    "

        print(root.name)

        if root.left or root.right:
            print_tree(root.left, indent, False)
            print_tree(root.right, indent, True)

def print_ancestors(root, creature):
    if root is None:
        return False
    if root.name == creature:
        return True
    if print_ancestors(root.left, creature) or print_ancestors(root.right, creature):
        print(root.name)
        return True
    return False


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
            print(f"{child_name.upper()} has been added to the tree.")
        else:
            print("That parent creature does not exist.")

    def search(self, root, key):
        if root is None or root.name == key:
            return root
        left_search = self.search(root.left, key)
        if left_search is not None:
            return left_search
        return self.search(root.right, key)

    # Fixed print_specific to print the ancestors of a creature
    def print_specific(self, creature_name):
        if not self.root:
            print("There aren't any creatures in the tree yet.")
            return
        print(f"Ancestors of {creature_name}:")
        if not print_ancestors(self.root, creature_name):
            print(f"{creature_name} does not exist in the tree.")

    def print_all(self):
        if self.root:
            print_tree(self.root)
        else:
            print("There aren't any creatures in the tree yet.")

def menu():
    app = App()

    while True:
        print()
        print('======= Menu =======')
        print('1) Add Root Creature')
        print('2) Add Creature')
        print('3) Print All')
        print("4) Print A Creature's Ancestors")
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
                print("Invalid side input. Use 'L' or 'R.'")

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
