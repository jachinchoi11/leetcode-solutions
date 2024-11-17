# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        # run the dfs on the root.left and root,right 
        # essentially we can map the paths onto an array and we get the max value from both 
        self.dfs(root, -float('inf'))
        return self.count 


    def dfs(self, root, minValue):
        if root.val >= minValue:
            self.count += 1
        if root.left:
            self.dfs(root.left, max(root.val, minValue))
        if root.right:
            self.dfs(root.right, max(root.val, minValue))
    