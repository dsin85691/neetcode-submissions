# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = None
        min_diff = float("inf")

        def dfs(root, res, min_diff): 
            if root is None: 
                return res
            
            abs_diff = abs(target - root.val) 
            if min_diff > abs_diff: 
                min_diff = abs_diff
                res = root 

            left_min  = dfs(root.left, res, min_diff) 
            res = left_min 
            right_min = dfs(root.right, res, min_diff)
            return right_min

        res = dfs(root, res, min_diff)
        return res.val