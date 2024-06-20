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
      self.head = new_node
    else:
      curr = self.head

      while curr.next is not None:
         curr = curr.next
      
      curr.next = new_node
    return self.traverse()
    
  def traverse(self):
    curr = self.head
    if curr is None:
      print('Linked List is empty')
      return
    while curr is not None:
      print(curr.value, end= " -> ")
      curr = curr.next
    print('None')
    return
    
  

ll = LinkedList()
ll.add_node('a')
# ll.add_node('b')
# ll.traverse()

