class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path that uses this node as the highest point
            self.best = max(
                self.best,
                node.val + left + right
            )

            # Return best downward path
            return node.val + max(left, right)

        dfs(root)
        return self.best