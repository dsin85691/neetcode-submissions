# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = -float("inf")
        def dfs(root, total_sum, num_nodes): 
            nonlocal max_avg
            if root is None: 
                return (0, 0)
            
            left_sum, num_left = dfs(root.left, total_sum, num_nodes) 
            right_sum, num_right = dfs(root.right, total_sum, num_nodes) 

            final_sum, final_num = left_sum + right_sum + root.val, num_left + num_right + 1
            max_avg = max(round(final_sum / final_num, 5), max_avg)
            # Total sum of left, right and root val
            return final_sum, final_num
        dfs(root, 0, 0) 
        return max_avg