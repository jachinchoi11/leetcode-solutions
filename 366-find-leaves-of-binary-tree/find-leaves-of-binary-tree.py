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

        res = defaultdict(list)

        if not root:
            return res
        
        self.dfs(root, res)
        return list(res.values())
    
    def dfs(self, curr_node, res):
        if not curr_node:
            return 0
        left_length = self.dfs(curr_node.left, res)
        right_length = self.dfs(curr_node.right, res)
        level = 1 + max(left_length, right_length)

        res[level].append(curr_node.val)
        return level

            
