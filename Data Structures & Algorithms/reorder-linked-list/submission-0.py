# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # recursion-stack 
        # def dfs(start, end) -
        # start - 1, end - 6
        # 1 --> 6 (push 6 before 1) 
        # start - 2, end - 5 (push 5 before 2) 
        # start - 3, end - 4 (push 4 before 3) 
        # 0, 6, 1, 5, 2, 4, 3 (This is how you get reordering with recursion) 
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None



