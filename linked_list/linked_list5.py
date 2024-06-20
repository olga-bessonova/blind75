class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def add_node(self, value):
    new_node = Node(value)

    if self.head == None:
      self.head = value
    else:
      curr = self.head

      while curr.next is not None:
         curr = curr.next
      
      curr.next = new_node

      return traverse(self)
    
    def traverse(self):
      curr = self.head

      while curr.next is not None:
        print(curr.value, " -> ")
        curr = curr.next
      print("None")

