# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] 


        def postOrder(node): 
            if node is None: 
                return
            
            postOrder(node.left) # left traversal
            postOrder(node.right) # Right traversal
            res.append(node.val) # post order traversal

        postOrder(root)
        return res