# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # essentially what we want to do here is to do a preorder travesal, as we go donw, 
        # we will pass in a [], 0 to start off, and it will add the curr.value and curr.value to our array
        # we will then do a check of if it is equal to or over, in that case we can just keep on backtracking 

        # and then if it does hit, we can save a version of that to a global varibale

        res = []
        if not root:
            return []

        def dfs(curr_node, currList, currSum):
            if not curr_node:
                return
            currList.append(curr_node.val)
            currSum += curr_node.val
            if currSum == targetSum and not curr_node.left and not curr_node.right:
                res.append(list(currList))
            
            dfs(curr_node.left, currList, currSum)
            dfs(curr_node.right, currList, currSum)
            currSum -= curr_node.val
            currList.pop()
        dfs(root, [], 0)
        return res
        