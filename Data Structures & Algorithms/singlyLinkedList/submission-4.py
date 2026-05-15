class ListNode: 
    def __init__(self, val): 
        self.val = val 
        self.next = None 

class LinkedList:
    
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0 

    def get(self, index: int) -> int:
        # Check for valid index
        if index < 0 or index >= self.length: 
            return -1 
        tmp = self.head
        # Traverse to the node at the specified index
        while index > 0: 
            tmp = tmp.next
            index -= 1 
        return tmp.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) 

        if self.head is None: 
            self.head = new_node 
            self.tail = self.head 
        else: 
            tmp = self.head 
            self.head = new_node 
            self.head.next = tmp 
        
        self.length+=1 

    def insertTail(self, val: int) -> None:

        if self.tail is None: 
            self.insertHead(val)
        else: 
            self.tail.next = ListNode(val) 
            self.tail = self.tail.next
            self.length+=1 
        
    def remove(self, index: int) -> bool:
        # Check for valid index
        if index < 0 or index >= self.length: 
            return False
        
        # Remove the head
        if index == 0: 
            self.head = self.head.next
            if self.length == 1:
                # If only one element was present, update tail as well
                self.tail = None
        else: 
            tmp = self.head
            # Traverse to the node just before the one to remove
            while index > 1: 
                tmp = tmp.next 
                index -= 1 

            # Remove the target node
            node_to_remove = tmp.next
            tmp.next = node_to_remove.next
            
            # Update tail if the last node was removed
            if node_to_remove == self.tail:
                self.tail = tmp

        self.length -= 1
        return True 


    def getValues(self) -> List[int]:
        arr_linked_list = [] 
        tmp = self.head 
        while tmp is not None:
            arr_linked_list.append(tmp.val)
            tmp = tmp.next
        return arr_linked_list
