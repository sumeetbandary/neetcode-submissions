class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        
        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursively invert the child subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root