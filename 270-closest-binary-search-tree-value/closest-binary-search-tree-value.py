# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        closest_value = [root.val, abs(target - root.val)]

        def traverse(node, closest_value):
            if not node:
                return
            curr_diff = abs(target- node.val)

            if curr_diff < closest_value[1]:
                closest_value[0] = node.val
                closest_value[1] = curr_diff
            
            elif curr_diff == closest_value[1]:
                closest_value[0] = min(closest_value[0], node.val)
            
            if node.val > target:
                traverse(node.left, closest_value)
            if node.val < target:
                traverse(node.right, closest_value)
        
        traverse(root, closest_value)
        return closest_value[0]