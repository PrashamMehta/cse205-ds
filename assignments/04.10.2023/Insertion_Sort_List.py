class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  

        sorted_head = ListNode(None) 
        current = head  
        while current:
        
            next_node = current.next

          
            prev, sorted_node = None, sorted_head
            while sorted_node and (sorted_node.val is not None and sorted_node.val < current.val):
                prev, sorted_node = sorted_node, sorted_node.next


            while sorted_node and sorted_node.val is None:
                prev, sorted_node = sorted_node, sorted_node.next


            if not prev:
                sorted_head = current
            else:
                prev.next = current
            current.next = sorted_node

      
            current = next_node

        return sorted_head.next  
