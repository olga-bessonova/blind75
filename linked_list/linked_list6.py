import math

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
      curr = curr.next
      
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
  
  def mid_search(self):
    hash = {}
    count = 0
    curr = self.head
    if curr is None:
      return count
    
    while curr is not None:
      hash[count] = curr.value 
      count += 1
      curr = curr.next
    
    return hash[int(math.ceil((count-1) / 2))]    
  
  def delete(self, value):
    curr = self.head
    prev = None
    # count = 0
    if curr is None:
      return 'Linked List is empty'
    
    while curr is not None:
      if curr.value == value:
        
        if curr.next is None:
          self.head = curr.next
          return 'The head was deleted. Linked List is empty'
        prev.next = curr.next
        # print('heeeeello')
        break
      prev = curr
      curr = curr.next
      # count += 1
      # print('count = ', count)
    
    return self.traverse()


ll = LinkedList()
ll.add_nodes(['a','b','c','d','e'])
ll.add_nodes(['xxxx','gg','a'])
ll.traverse()
# print(ll.mid_search())

# ll2 = LinkedList()
# ll2.add_nodes(['a'])
# ll2.traverse()
# print(ll2.delete('a'))