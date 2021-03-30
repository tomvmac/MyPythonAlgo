# Find Kth Largest Value in BST

# Write a function that takes in a Binary Search Tree (BST) and a positive integer k and returns the kth largest contained in the BST.

# You can assume that there will be only integer values in the BST and that k is less than or equal to the number of nodes in the tree.

# Also, for the purpose of this question, duplicate integers will be treated as distinct values.  In other words, the second largest value in
# a BST containing {5, 7, 7} will be 7 and not 5.

# General Strategy:
# 1. Perform In Order BST Traversal (Left, Root, Right)
# 2. Append value to array
# 3. Since array is already sorted due to In Order, grab the kth element from the end and return

# Time: O(n)
# Space: O(n)

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues)-k]


def inOrderTraverse(node, sortedNodeValues):
    if node is None:
        return

    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)


# Driver Code
root = BST(15)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(20)
root.right.left = BST(17)
root.right.right = BST(22)

k=3

print(findKthLargestValueInBst(root, 3))