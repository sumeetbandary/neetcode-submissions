class Solution:

    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Skip the nth node from the end
        left.next = left.next.next

        return dummy.next