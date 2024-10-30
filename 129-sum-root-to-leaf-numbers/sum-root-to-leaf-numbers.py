# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        self.sum = 0
        self.dfs(root, res)
        return self.sum

    def dfs(self, root, res):
        if not root:
            return 

        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

        if not root.left and not root.right:
            self.sum += int("".join(map(str, res)))
        res.pop()


