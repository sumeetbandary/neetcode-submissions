# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Both nodes are None, trees are identical so far
        if not p and not q:
            return True
        
        # One is None and the other is not, trees are not identical
        if not p or not q:
            return False
        
        # Values must match, and both left and right subtrees must be the same
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)