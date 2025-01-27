# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        # so i think we can do a dfs, where in each sub problem we can add, as we go and see if we ever reach the value 

        # this can be a preorder traversal, as we want to evaluate the values, before we go down 
        # we can have two base cases, one being if the sum is already bigger than the targetSum, we will terminate it and return False
        # if the value is a leaf node and the value == targetSum, return True there 

        # if the value is the value, but not a leaf node, we can also terminate ealeir where 

        # if not, we will add to the currSum and and then pass it in as a parameter, so we would do curr_node, currSum 

        # since it recurses back, it should redo those values, and we should not have to backtrack
        if not root:
            return False
        return self.preDfs(root, 0, targetSum)
        
    def preDfs(self, curr_node, curr_sum, targetSum):
        curr_sum += curr_node.val
        if not curr_node.left and not curr_node.right:
            if curr_sum == targetSum:
                return True
            else:
                return False

        left, right = False, False
        if curr_node.left:
            left = self.preDfs(curr_node.left, curr_sum, targetSum)
        if curr_node.right:
            right = self.preDfs(curr_node.right, curr_sum, targetSum)

        return left or right


