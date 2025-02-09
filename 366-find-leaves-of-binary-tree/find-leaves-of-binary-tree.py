# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # intuition - use the height of the certain tree to map the leaves 
        # but the thing is do we preallocate it, or do we just append and reverse it at the end
        res = []
        if not root:
            return res
        
        self.dfs(root, res)

        return res
    
    def dfs(self, curr_node, res):
        if not curr_node:
            return -1
        level = 1 + max(self.dfs(curr_node.left, res), self.dfs(curr_node.right, res))
        if len(res) <= level:
            res.append([])
        res[level].append(curr_node.val)
        return level

            
