class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

# Example usage
ll = LinkedList()
ll.add_node(555)
ll.add_node(556)
ll.add_node(557)

print("Original list:")
ll.traverse()

ll.reverse()
print("Reversed list:")
ll.traverse()
