# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = [] 

        def dfs(node, path): 
            if node is None: 
                return 0 

            is_good = 0
            # Check the path to the node 
            if self.is_good(node, path): 
                is_good = 1
            
            path.append(node.val) # append node to the path
            good_left, good_right = 0, 0 # Initialize these to be 0
            if node.left: 
                good_left = dfs(node.left, path) 
            if node.right: 
                good_right = dfs(node.right, path) 
            path.pop() # Remove the node 
            # Count the number of good nodes from left subtree + right subtree and check the middle node
            return is_good + good_left + good_right
        return dfs(root, path)
        
    def is_good(self, node, path): 
        for node_val in path: 
            if node_val > node.val: 
                return False 
        return True