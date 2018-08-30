"""Problem:
   Given the root to a binary tree, return the deepest node.
"""

def deepest(node):
    if node and not node.left and not node.right:
        return (node, 1) # Leaf and its depth
    if not node.left: # Then the deepest node is on the right subtree
        return increment_depth(deepest(node.right))
    elif not node.right: # Then the deepest node is on the left subtree
        return increment_depth(deepest(node.left))
    return increment_depth(
            max(deepest(node.left), deepest(node.right),
                    key=lambda x: x[1])) # Pick higher depth tuple and then increment its depth
#In this case, max() will return the element in that array whose second element (x[1]) 
#is larger than all of the other elements' second elements.

def increment_depth(node_depth_tuple):
    node, depth = node_depth_tuple
    return (node, depth + 1)
