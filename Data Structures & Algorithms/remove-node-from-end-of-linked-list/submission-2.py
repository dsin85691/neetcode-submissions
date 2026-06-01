class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length - n = # of pointers in front of head 

        # Iterate through elem in the list
        tmp = head
        length = 0 
        while tmp is not None: # O(n) 
            length+=1 
            tmp = tmp.next

        # Target index to remove is length - n
        if length == n:
            return head.next

        i = 0
        tmp_ptr = head
        while i < length - n - 1: # O(n) 
            tmp_ptr = tmp_ptr.next 
            i+=1

        # O(1)
        prev_ptr, nth_node, next_ptr = tmp_ptr, tmp_ptr.next, tmp_ptr.next.next
        nth_node.next = None # Remove nth node 
        prev_ptr.next = next_ptr # Move prev ptr to the next ptr 

        return head