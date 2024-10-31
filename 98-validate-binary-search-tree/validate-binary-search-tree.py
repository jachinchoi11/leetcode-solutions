# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True
        self.res = []
        self.dfs(root)
        return self.isValid
    
    def dfs(self, root): 
        if not root:
            return
        self.dfs(root.left)
        if self.res and root.val <= self.res[-1]:
            self.isValid = False
        self.res.append(root.val)
        self.dfs(root.right)
