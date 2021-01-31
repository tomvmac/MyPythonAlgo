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

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            # Keep looking until found min on right child
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        # Deleting nodes requires attention to the following steps:
        # 1. Find node with key

        # Conditions
        # 1. Node has no children or leaf node:
        #    a.  Delete node or root if there no children or leaf nodes by removing link from parent to leaf node
        # 2. Node has one child or leaf node:
        #    a. Make parent of node point to node's child
        #    b. Point node to None
        # 3. Node has two children or leaf nodes (choose one):
        #    a. If Choose left child
        #        i. Find the max value from the left child
        #        j. Keep traversing left until you find a node with no right child = max value
        #        k. Copy max value to node value
        #        l. Remove max node by pointing it's parent to max node's child and point max node left child to None
        #    b. If Choose right child
        #        i. Find the min value from the right child
        #        j. Keep traversing left until you find a node with no left child = min value
        #        k. Copy min value to node value
        #        l. Remove min node by pointing it's parent to min node's child and point min node right child to None

        if curr:
            if key == curr.data:
                print("Found node to delete")
                if curr.left_child and curr.right_child:
                    # both left and right child exits
                    min_child = self.min_right_subtree(curr.right_child)
                    # Once found, copy data
                    curr.data = min_child.data
                    # set parent to point to child next
                    self._delete_val(curr.right_child, curr, False, curr.data)

                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        # no child
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    # no left child
                    if prev:
                        # Make parent point to curr node right child
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                elif curr.right_child == None:
                    # no right child
                    if prev:
                        # Make parent point to curr node right child
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)

        else:
            print(f"{key} not found in Tree.")


# Execution Code

tree = BSTDemo()

# tree.insert("F")
# print(tree.root.data)

# tree.insert("C")
# print(tree.root.left_child.data)

# tree.insert("G")
# print(tree.root.right_child.data)

# tree.insert("A")
# print(tree.root.left_child.left_child.data)

# tree.insert("B")
# print(tree.root.left_child.left_child.right_child.data)

# tree.insert("K")
# print(tree.root.right_child.right_child.data)


# tree.insert("H")
# print(tree.root.right_child.right_child.left_child.data)


# tree.insert("E")
# print(tree.root.data)
#
# tree.insert("D")
# print(tree.root.data)
#
# tree.insert("I")
# print(tree.root.data)
#
# tree.insert("M")
# print(tree.root.data)
#
# tree.insert("J")
# print(tree.root.data)
#
# tree.insert("L")
# print(tree.root.data)

# print("in order (left, root, right)\n")
# tree.in_order()
# print("\n------------------------------\n")
#
# print("pre order (root, left, right)\n")
# tree.pre_order()
# print("\n------------------------------\n")
#
# print("post order (left, right, root)\n")
# tree.post_order()

# print("search for E")
# print(tree.find_val("E"))
#
# print("search for J")
# print(tree.find_val("J"))
#
# print("search for Z")
# print(tree.find_val("Z"))

# print("\n------------------------------\n")
# print("delete Z\n")
#
# tree.in_order()
# tree.del_val("Z")
# tree.in_order()

print("\n------------------------------\n")
print("delete node scenarios\n")

tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("H")
tree.insert("E")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")

print("Test deleting C lead node which is left child of parent")
tree.in_order()
tree.delete_val("C")
tree.in_order()
print("Test deleting G lead node which is right child of parent")
tree.in_order()
tree.delete_val("G")
tree.in_order()
print("Test deleting F parent/root node which has one child")
tree.in_order()
tree.delete_val("F")
tree.in_order()
print("Test deleting A parent/root node which has no child")
tree.in_order()
tree.delete_val("A")
tree.in_order()
print("Test deleting K")
tree.in_order()
tree.delete_val("K")
tree.in_order()
tree.delete_val("Z")


