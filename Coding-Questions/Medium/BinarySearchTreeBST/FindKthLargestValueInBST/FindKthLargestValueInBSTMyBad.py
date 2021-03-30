# Find Kth Largest Value in BST

# Write a function that takes in a Binary Search Tree (BST) and a positive integer k and returns the kth largest contained in the BST.

# You can assume that there will be only integer values in the BST and that k is less than or equal to the number of nodes in the tree.

# Also, for the purpose of this question, duplicate integers will be treated as distinct values.  In other words, the second largest value in
# a BST containing {5, 7, 7} will be 7 and not 5.

# General Strategy:
# 1. Perform reverse In Order Traversal (Right, Value, Left)
# 2. Keep track of nodesVisited, once it equal k, return

# Time: O(n)
# Space: O(1)

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    nodesVisited = 0
    nodeKValue = 0
    return reverseInOrderTraverse(tree, k, nodesVisited, nodeKValue)



def reverseInOrderTraverse(node, k, nodesVisited, nodeKValue):
    if node is None:
        return

    if nodesVisited >=k:
        return nodeKValue

    reverseInOrderTraverse(node.right, k, nodesVisited, nodeKValue)
    if nodesVisited < k:
        nodeKValue = node.value
        nodesVisited += 1
        reverseInOrderTraverse(node.left, k, nodesVisited, nodeKValue)


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
