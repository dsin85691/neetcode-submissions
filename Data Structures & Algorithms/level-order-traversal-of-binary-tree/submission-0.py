# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return [] 

        queue = deque() 
        list_of_elems = [[root.val]] 
        queue.append(root) 
        new_level = [] 

        while len(queue) > 0: 
            root_elem = queue.popleft() 

            if root_elem.left:
                new_level.append(root_elem.left) 
            if root_elem.right:
                new_level.append(root_elem.right)

            if len(queue) == 0 and len(new_level) > 0: 
                list_of_elems.append([node.val for node in new_level]) 
                queue.extend(new_level)
                new_level = [] 
        
        return list_of_elems