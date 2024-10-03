class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1  
            list1 = list1.next    
        else:
            current.next = list2  
            list2 = list2.next    
        current = current.next    

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next
# Example 1:
# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

result = mergeTwoLists(list1, list2)

# Print merged list
while result:
    print(result.val, end=" -> ")
    result = result.next
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 
