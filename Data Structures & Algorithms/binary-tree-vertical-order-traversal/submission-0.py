# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_dict = {}

        def dfs(root, row, col_class): 
            if root is None: 
                return

            if col_class not in col_dict: 
                col_dict[col_class] = [] 

            col_dict[col_class].append((row, root.val))
            dfs(root.left, row + 1, col_class-1) 
            dfs(root.right, row + 1, col_class+1) 

        dfs(root, 0, 0) 
        res = [] 
        for key in sorted(col_dict.keys()): 
            col_vals = sorted(col_dict[key], key=lambda x: x[0])
            res.append([val for _, val in col_vals])
        return res
