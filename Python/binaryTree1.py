class Node:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def serialize(root):
   s = ""
   s += root.val
   if(not root.left):
      s += "-"
      s += serialize(root.left)
   if(not root.right):
      s += "-"
      s += serialize(root.right)
   return s
   
def deserialize(s):
   def deserializeHelper(node,nodes):
      val = nodes.pop()
      if not val:
         return
      node = Node(val)
      temp = nodes[len(nodes)-1]
      sub = temp.split(".")
      if(sub == "left"):
         node.left = deserializeHelper(node.left,nodes)
      temp = nodes[len(nodes)-1]
      sub = temp.split(".")
      if(sub == "right"):
         node.right = deserializeHelper(node.left,nodes)
      return node
      
      """temp = sub.split(".")
      #left,left \/ = 1
      if temp[len(temp)-1] == "left":
         node = Node("""
   nodes = s.split("-")
   #root,left,left.left,right pre
   #left.left,left,root,right in
   #left.left,left,right,root post
   for i in range(len(nodes)):
      deserializeHelper(nodes[i])
      

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

#I couldn't get this one in time.