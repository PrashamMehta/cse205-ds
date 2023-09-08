class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
      
        def get_length(head):
            length = 0
            current = head
            while current:
                length += 1
                current = current.next
            return length
        
       
        lenA = get_length(headA)
        lenB = get_length(headB)
        
       
        ptrA, ptrB = headA, headB
        
        
        if lenA > lenB:
            for _ in range(lenA - lenB):
                ptrA = ptrA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                ptrB = ptrB.next
        
        
        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        
      
        return ptrA