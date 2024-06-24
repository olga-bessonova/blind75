class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # creates nodes out of add array of values and adds nodes at the end of the linked list
  def add_nodes(self, arr_values): # arr_values = ['a','b','c']
    # check is head is None
    if self.head is None:
      self.head = Node(arr_values[0])
      curr = self.head
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = Node(arr_values[0])
     
    for i in range(1, len(arr_values)):
      new_node = Node(arr_values[i])
      curr.next = new_node
      curr = new_node
    curr.next = None

  # def add_node(self, value):


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
  
  delete


ll = LinkedList()
ll.add_nodes(['a','b','c'])
ll.traverse()