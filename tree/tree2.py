class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left_child = None
    self.right_child = None

  def insert_left(self, value):
    if self.left_child == None:
      self.left_child = BinaryTree(value)
    else:
      new_node = BinaryTree(value)
      new_node.left_child = self.left_child
      self.left_child = new_node

  def insert_right(self, value):
    if self.right_child is None:
      self.right_child = BinaryTree(value)
    else:
      new_node = BinaryTree(value)
      new_node.right_child = self.right_child
      self.right_child = new_node.right_child

  
  def dfs_traverse(self, target):
    # print(self.value)
    if self.value == target:
      return print('Target is found')
    
    if self.left_child:
     self.left_child.dfs_traverse(target)
      
    
    if self.right_child:
      self.right_child.dfs_traverse(target)

    # return 'Target is not found'
    

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')
b_node = a_node.left_child
c_node = a_node.right_child

b_node.insert_left('d')
b_node.insert_right('e')

c_node.insert_left('f')
c_node.insert_right('g')

print(a_node.dfs_traverse('h'))
#    a
#   b c
# d e f g

