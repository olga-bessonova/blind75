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

    