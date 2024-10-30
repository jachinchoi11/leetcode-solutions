# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        self.ans = []
        self.dfs(root, res)
        add = 0
        for batch in self.ans:
            s = "".join(map(str, batch))
            add += int(s)
        return add

    def dfs(self, root, res):
        if not root:
            return 

        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

        if not root.left and not root.right:
            self.ans.append(list(res))
        res.pop()


