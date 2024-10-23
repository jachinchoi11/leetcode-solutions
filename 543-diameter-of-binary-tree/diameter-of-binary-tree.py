# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter = 0
        self.maxdfs(root)
        return self.maxdiameter


    def maxdfs(self, root):
        if not root:
            return 0 
        left = self.maxdfs(root.left)
        right = self.maxdfs(root.right)

        self.maxdiameter = max(self.maxdiameter, left + right)
        return 1 + max(left, right)
    
    # need it to take the min