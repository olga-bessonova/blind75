class Reverse:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next  # Temporarily store the next node
            curr.next = prev  # Reverse the link
            prev = curr       # Move prev pointer forward
            curr = nxt        # Move curr pointer forward

        return prev  # prev will be the new head of the reversed list
