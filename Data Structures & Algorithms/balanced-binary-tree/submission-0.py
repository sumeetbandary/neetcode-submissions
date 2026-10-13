# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node):
            # Base case: an empty tree is balanced and has a height of 0
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Check if current subtree is balanced:
            # 1. Left subtree must be balanced
            # 2. Right subtree must be balanced
            # 3. Height difference between left and right must be <= 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # Return the balance status and the height of the current node
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]