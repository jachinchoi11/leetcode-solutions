# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # we're going to essetnially find where any of the sums are going to be hidden
        # i think maybe we need to use like a hashmap of numbers, as we go
        # if we've already seen it before we would add to it and be like oh we can take away this number 
        # so maybe it woudl moreso be a running collection of sums in the hashset 
        # we would check if currSum - targetSum is in the thing, if it is we woudl add one to our answer

        sum_tracker = defaultdict(int)
        self.res = 0
        sum_tracker[0] = 1
        def dfs(curr_node, curr_sum):
            if not curr_node:
                return
            curr_sum += curr_node.val
            
            if curr_sum - targetSum in sum_tracker:
                self.res += sum_tracker[curr_sum - targetSum]
            sum_tracker[curr_sum] += 1
            dfs(curr_node.left, curr_sum)
            dfs(curr_node.right, curr_sum)

            sum_tracker[curr_sum] -= 1

        dfs(root, 0)
        return self.res




        