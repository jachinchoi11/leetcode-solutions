# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.dfs(root, p,q)

    def dfs(self, root, p, q):
        if not root:
            return
        if p.val > root.val and q.val > root.val:
            return self.dfs(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.dfs(root.left, p, q)
        else:
            return root

