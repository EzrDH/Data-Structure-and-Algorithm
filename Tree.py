from abc import ABC, abstractmethod

class Tree(ABC):

    class Position:

        @abstractmethod
        def element(self):
            raise NotImplementedError()

        def __eq__(self, other):
            raise NotImplementedError()

        def __ne__(self, other):
            return not (self == other) 

    @abstractmethod
    def root(self):
        raise NotImplementedError()

    @abstractmethod
    def parent(self, p):
        raise NotImplementedError()

    @abstractmethod
    def num_children(self, p):
        raise NotImplementedError()

    @abstractmethod
    def children(self, p):
        raise NotImplementedError()

    @abstractmethod
    def __len__(self):
        raise NotImplementedError()

class TreeNode(Tree.Position):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def element(self):
        return self.data

    def __eq__(self, other):
        return isinstance(other, type(self)) and other.data == self.data

class Tree(Tree):
    def __init__(self):
        self.root_node = None
        self.size = 0

    def root(self):
        return self.root_node

    def parent(self, p):
        return p.parent

    def num_children(self, p):
        return len(p.children)

    def children(self, p):
        return p.children

    def __len__(self):
        return self.size

    def add_node(self, data, parent=None):
        new_node = TreeNode(data)
        if parent is None:
            if self.root_node is not None:
                raise ValueError("Tree is not empty. Cannot add a new root.")
            self.root_node = new_node
        else:
            parent.children.append(new_node)
            new_node.parent = parent
        self.size += 1
        return new_node

    def print_tree(self, node, depth=0):
        prefix = "    " * depth + "|__" if depth > 0 else ""
        print(prefix + str(node.element()))
        for child in self.children(node):
            self.print_tree(child, depth + 1)

# Contoh penggunaan
tree = Tree()

# Menambahkan simpul-simpul ke dalam tree
root = tree.add_node("Root")
child1 = tree.add_node("Child 1", parent=root)
child2 = tree.add_node("Child 2", parent=root)
grandchild = tree.add_node("Grandchild", parent=child2)

# Menampilkan tree
tree.print_tree(tree.root())
