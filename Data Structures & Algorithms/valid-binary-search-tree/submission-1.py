class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # If we reach a None node, we default to True
        if root is None: 
            return True

        bst_left, bst_right = True, True
        
        if root.left: 
            # If the left subtree contains a value that is greater
            left_subtree_max = self.findMax(root.left)
            if left_subtree_max >= root.val: 
                return False 
            bst_left = self.isValidBST(root.left) 
        
        if root.right: 
            # If the min of the right subtree is less than, return False
            right_subtree_min = self.findMin(root.right)
            if right_subtree_min <= root.val: 
                return False 
            bst_right = self.isValidBST(root.right) 

        return bst_left and bst_right 

    def findMin(self, root): 
        tmp = root
        while tmp.left is not None: 
            tmp = tmp.left 
        return tmp.val 
    
    def findMax(self, root): 
        tmp = root 
        while tmp.right is not None: 
            tmp = tmp.right 
        return tmp.val