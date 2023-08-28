# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            print(curr)
            print(prev)
            # print(curr.next)
            nxt = curr.next
            print(nxt)
            curr.next = prev
            prev = curr
            curr = nxt
        return prev