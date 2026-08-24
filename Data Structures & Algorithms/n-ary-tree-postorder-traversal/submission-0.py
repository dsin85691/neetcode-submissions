"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        postorder=[] 
        visited = set() 
        def dfs(root): 
            if root is None: 
                return 

            if root in visited:
                return 
            
            visited.add(root)
            for i in range(len(root.children)): 
                dfs(root.children[i])
            postorder.append(root.val)
        dfs(root)
        return postorder