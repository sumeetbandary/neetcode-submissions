class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev       # Reverse pointer
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
            
        return prev