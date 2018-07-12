"""Problem: 
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def init(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

Note: Its good to remember that preorder tree walks are for copying/ making trees
and postorder tree walks are for deleting trees.
"""

class Node:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def serialize(root):
   s = ""
   s += root.val
   if(root.left != None):
      s += "-"
      s += serialize(root.left)
   if(root.right != None):
      s += "-"
      s += serialize(root.right)
   return s
   
def deserialize(s):
   def deserializeHelper(node,nodes):
      val = nodes.pop(0)
      print(nodes)
      print(val)
      node = Node(val)
      if(nodes != []):
         temp = nodes[0]
         print(temp)
         sub = temp.split(".")
         print(sub)
         if(sub[len(sub)-1] == "left"):
            node.left = deserializeHelper(node.left,nodes)
      if(nodes != []):
         temp = nodes[len(nodes)-1]
         sub = temp.split(".")
         if(sub[len(sub)-1] == "right"):
            node.right = deserializeHelper(node.right,nodes)
      return node      
   nodes = s.split("-")   
   print(nodes)
   return deserializeHelper(None,nodes)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(deserialize(serialize(node)).left.left.val == 'left.left')
#assert deserialize(serialize(node)).left.left.val == 'left.left'

#I couldn't get this one in time. 

#root,left,left.left,right pre
#left.left,left,root,right in
#left.left,left,right,root post
