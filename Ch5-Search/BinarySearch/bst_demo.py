class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                # recursively call itself
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                # recursively call itself
                self._insert(curr.left_child, key)

    def in_order(self):
        # left, root, right
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            # recursively traverse left
            self._in_order(curr.left_child)
            # print root
            print(curr.data, end=" ")
            # recursively traverse right
            self._in_order(curr.right_child)

    def pre_order(self):
        # root, left, right
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        if curr:
            # print root
            print(curr.data, end=" ")
            # left
            self._pre_order(curr.left_child)
            # right
            self._pre_order(curr.right_child)

    def post_order(self):
        # left, right, root
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        if curr:
            # left
            self._pre_order(curr.left_child)
            # right
            self._pre_order(curr.right_child)
            # root
            print(curr.data, end=" ")


    def find_val(self, key):
        # O(h), O(long(n))
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        # check for existing of element
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return "Value not found in tree"

# Execution Code

tree = BSTDemo()

tree.insert("F")
# print(tree.root.data)

tree.insert("C")
# print(tree.root.left_child.data)

tree.insert("G")
# print(tree.root.right_child.data)

tree.insert("A")
# print(tree.root.left_child.left_child.data)

tree.insert("B")
# print(tree.root.left_child.left_child.right_child.data)

tree.insert("K")
# print(tree.root.right_child.right_child.data)


tree.insert("H")
# print(tree.root.right_child.right_child.left_child.data)


tree.insert("E")
# print(tree.root.data)
#
tree.insert("D")
# print(tree.root.data)
#
tree.insert("I")
# print(tree.root.data)
#
tree.insert("M")
# print(tree.root.data)
#
tree.insert("J")
# print(tree.root.data)
#
tree.insert("L")
# print(tree.root.data)

print("in order (left, root, right)\n")
tree.in_order()
print("\n------------------------------\n")

print("pre order (root, left, right)\n")
tree.pre_order()
print("\n------------------------------\n")

print("post order (left, right, root)\n")
tree.post_order()

print("search for E")
print(tree.find_val("E"))

print("search for J")
print(tree.find_val("J"))

print("search for Z")
print(tree.find_val("Z"))
