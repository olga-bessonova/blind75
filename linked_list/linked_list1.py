class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        if not curr_node:
            return
        if prev:
            prev.next = curr_node.next
        else:
            self.head = curr_node.next

    def delete_node_at_pos(self, pos):
        if pos < 0 or pos > self.get_size():
            return
        if pos == 0:
            self.head = self.head.next
            return
        curr_node = self.head
        prev = None
        for i in range(pos):
            prev = curr_node
            curr_node = curr_node.next
        if prev:
            prev.next = curr_node.next
        else:
            self.head = curr_node.next

    def get_size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.print_list()
    print()
    llist.prepend(5)
    llist.print_list()
    print()
    llist.insert_after(llist.head.next, 6)
    llist.print_list()
    print()
    llist.delete_node(3)
    llist.print_list()
    print()
    llist.delete_node_at_pos(2)
    llist.print_list()
    print()
    print(llist.get_size())
    print(llist.search(6))