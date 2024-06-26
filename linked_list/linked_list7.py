class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):
    curr = self.head
    if not curr:
      self.head = Node(value)
      return

    while curr.next is not None:
      curr = curr.next

    curr.next = Node(value)
  
  
  def traverse(self):
    curr = self.head
    if curr is None:
      return None
    
    while curr is not None:
      print(curr.value, end=' -> ')
      curr = curr.next
  

  def delete(self, remove_value):
    curr = self.head
    prev = None
    if curr is None:
      return 'The Linked List is empty'
    
    if curr.value == remove_value:
      self.head = curr.next
      print(remove_value, 'was removed')
      return self.traverse()
    while curr is not None:
      if curr.value == remove_value:
        prev.next = curr.next
        print(remove_value, 'was removed')
        return self.traverse()
      else:
        prev = curr
        curr = curr.next
    return print(remove_value, 'was not found')
    
  
  def insert(self, inserted_value, position):
    # the head has a position 1. Insert at position 1 means to insert to the head
    curr = self.head
    prev = None
    forw = None
    counter = 0

    if curr is None:
      if position == 1:
        self.append(inserted_value)
      else:
        print('not possible to insert at position', position)
        return self.traverse()
    
    # while counter != position:-, 


l = LinkedList()
l.append('a')
l.append('b')
l.append('c')
l.append('d')
l.append('e')
l.append('f')
l.append('g')
print(l.traverse())

print(l.delete('a'))

    