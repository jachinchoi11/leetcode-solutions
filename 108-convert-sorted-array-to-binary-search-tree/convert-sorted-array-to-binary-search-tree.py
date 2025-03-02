# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # nums array in ascending order 
        # for a height balanced binary search tree, basically the inorder traversal would be that 
        # so if we create our root straight down the middle 

        # we can guarantee that bot sides will have the same height
            # if we split the tree into half

        # so we can have a recursive method that i can give two bounds to 
            # the left and the right 
                #  we can do exclusive of the midpoint 
            # and then that will be hte new root
            # point the parent pointer left to the left one 
                # point the parent pointer right to the right one

        def construct_tree(left, right):

            if left > right:
                return None
            
            middle_index = (left + right) // 2
            current_root = TreeNode(nums[middle_index])
            current_root.left = construct_tree(left, middle_index - 1)
            current_root.right = construct_tree(middle_index + 1, right)

            return current_root
        
        return construct_tree(0, len(nums) - 1)







