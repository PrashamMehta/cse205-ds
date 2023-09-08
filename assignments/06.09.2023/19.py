class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        first = dummy_head
        second = dummy_head

        
        for i in range(n + 1):
            first = first.next

        
        while first is not None:
            first = first.next
            second = second.next

       
        second.next = second.next.next

        return dummy_head.next