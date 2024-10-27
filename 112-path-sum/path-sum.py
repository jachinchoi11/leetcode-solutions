# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0
        self.hasPathSum = False
        self.targetSum = targetSum
        self.dfs(root, sum)
        return self.hasPathSum


    def dfs(self, root, sum):
        if not root:
            return 0
        sum += root.val 
        if sum == self.targetSum and not root.left and not root.right:
            self.hasPathSum = True

        self.dfs(root.left, sum)
        self.dfs(root.right, sum)


