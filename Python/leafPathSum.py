class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def print_tree(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        current_level = next_level


def path_sum(root, s):
    # print(s, root.value, s - root.value)
    if root.left is None and root.right is None:
        # print(s - root.value == 0)
        return s - root.value == 0

    left_ans = False
    right_ans = False

    if root.left is not None:
        left_ans = path_sum(root.left, s - root.value)
    if root.right is not None:
        right_ans = path_sum(root.right, s - root.value)

    return left_ans or right_ans


rootNode = TreeNode(10)
rootNode.left = TreeNode(8)
rootNode.right = TreeNode(2)
rootNode.left.left = TreeNode(3)
rootNode.left.right = TreeNode(5)
rootNode.right.left = TreeNode(2)

print_tree(rootNode)
print("Begin output of path_sum()")
# print(path_sum(rootNode, 21))
# print(path_sum(rootNode, 23))
# print(path_sum(rootNode, 14))
# print(path_sum(rootNode, 11))
s = 23
for i in range(s + 1):
    if path_sum(rootNode, i):
        print("The sum %d is in tree" % i)
    else:
        print("The sum %d is not in the tree" % i)
