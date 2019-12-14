"""Problem:
   This problem was asked by Google.
   A unival tree (which stands for "universal value") is a tree where all nodes
   under it have the same value.
   Given the root to a binary tree, count the number of unival subtrees.
   For example, the following tree has 5 unival subtrees:
     0
    / \
   1   0
      / \
     1   0
    / \
   1   1
   The three 1 leaves, the one 0 leef, and the tree with 1's.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This isn't a very good picture of a tree, but it works.
def preOrderWalk(node, level=0):
    if node is None: return
    print('\t' * level, node.val)
    preOrderWalk(node.left, level + 1)
    preOrderWalk(node.right, level + 1)


# It was right to think pre-order. However a solution like this doesn't have enough logic.
"""
def univalTree(node,val):
   count = 0
   if node is None: return 0
   if node.val == val
     count += 1
   count += univalTreeHelper(node.left,node.val)
   count += univalTreeHelper(node.left,node.val)
   return count
"""
# Some extra stuff. Combine it forms a good solution
"""
def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
    if root is None:
        return True
    if root.value == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)
    return False
    
def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival(root) else left + right
"""


def count_unival_subtrees(root):
    count, _ = helper(root)
    return count


# Also returns number of unival subtrees, and whether it is itself a unival subtree.
# Runs in O(N)
def helper(root):
    if root is None:
        return 0, True
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
        if root.left is not None and root.val != root.left.val:
            return total_count, False
        if root.right is not None and root.val != root.right.val:
            return total_count, False
        return total_count + 1, True
    return total_count, False


node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
preOrderWalk(node)
print("There are", count_unival_subtrees(node), "univalTrees")
