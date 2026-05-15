# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0 

        if root is None: 
            return 0 
        
        depth+=1 
        depth1 = self.maxDepth(root.left) 
        depth2 = self.maxDepth(root.right)  

        max_depth = max(depth1, depth2) 
        depth+=max_depth

        return depth