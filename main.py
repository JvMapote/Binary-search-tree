class TreeExcer:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right
def insertData(temp,data):
   dataQueue = []
   dataQueue.append(temp)
   while (len(dataQueue)):
      temp = dataQueue[0]
      dataQueue.pop(0)
      if (not temp.left):
         temp.left = TreeExcer(data)
         break
      else:
         dataQueue.append(temp.left)
      if (not temp.right):
         temp.right = TreeExcer(data)
         break
      else:
         dataQueue.append(temp.right)
def create_tree(elements):
   Tree = TreeExcer(elements[0])
   for element in elements[1:]:
      insertData(Tree, element)
   return Tree

class Traversal(object):
   def inorderTraversal(self, root): 
      res, stack = [], []
      current = root
      while True:
         while current:
            stack.append(current)
            current = current.left
         if len(stack) == 0:
            return res
         node = stack[-1]
         stack.pop(len(stack)-1)
         if node.data != None:
            res.append(node.data)
         current = node.right
      return res
ob1 = Traversal()  
root = create_tree([10,5,15,2,7,20])
print(ob1.inorderTraversal(root)) 
