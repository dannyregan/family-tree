class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
    
    def info(self):
        return self.name

def insert(root, key, side):
    if root is None:
        return Node(key)
    if side == 'L':
        root.left = insert(root.left, key, side)
    else:
        root.right = insert(root.right, key, side)
    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
    

# The menu() acts directly with the App class which calls relevant functions to create instances of classes. It also houses functions relevant to printing animal information.
class App:
    # This list keeps track of all animal instances being made, regardless of their exact type (bear, elephant, penguin, or monkey).
    def __init__(self):
        self.creatures = []

    # The 'animal' variable represents an object from the menu.
    def add_creature(self, creature):
        self.creatures.append(creature)

    # Since the self.animals list contains objects, each 'animal' is a specific object while the 'animal_class' is the class type (Bear, Elephant, Penguin, Monkey), allowing us to call the info() method directly.
    def print_specific(self, animal_class):
        for animal in self.animals:
            if isinstance(animal, animal_class):
                print(animal.info())
    
    def print_all(self):
        for animal in self.animals:
            print(animal.info())

# need to look into the add_creature function from the start and move down from there

def menu():
    app = App()

    while len(app.creatures) == 0:
        print()
        print('======= Menu =======')
        print('1) Add Root Creature')
        print('0) Exit')
        print('====================')
        selection = input('Enter 1 to add a creature. ')

        if selection == '1':
            name = input('What\'s the creature\'s name? ')
            app.add_creature(Node(name))
            for creature in app.creatures:
                print(creature.info())
        elif selection == '0':
            break
        else:
            print('Invalid input.')

    while len(app.creatures) > 0:
        print()
        print('======= Menu =====')
        print('1) Add Creature')
        print('2) Print All')
        print('3) Print Specific')
        print('0) Exit')
        print('==================')
        selection = input('Enter 1 to add a creature. ')

        if selection == '1':
            parent = input('What\'s the parent\'s name: ')
            leftOrRight = input('Input L or R child: ').upper()
            if leftOrRight == 'L' or leftOrRight == 'R':
                name = input('What\'s the creature\'s name? ')
                for creature in app.creatures:
                    if creature.name == parent:
                        root = creature
                        insert(root, name, leftOrRight)
                        print(f"{name.upper()} has been added to the tree.")
            else:
                print('Invalid input.')
            app.add_creature(Node(name))
            # for creature in app.creatures:
            #     print(creature.info())
        elif selection == '0':
            break
        else:
            print('Invalid input.')
    
# =================================================
menu()