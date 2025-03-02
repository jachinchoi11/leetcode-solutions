# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        """# bfs version 

        queue = deque([root])

        while queue:
            curr_level = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if not curr_node:
                    curr_level.append(None)
                else:
                    curr_level.append(curr_node.val)
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            if curr_level != curr_level[::-1]:
                return False
        return True"""

        # dfs version 

        # we essentially want to check the nodes for the dfs

        return self.dfs(root.left, root.right)
        
    
    def dfs(self, left_side_node, right_side_node):

        if not left_side_node and not right_side_node:
            return True
        
        if not left_side_node or not right_side_node:
            return False
        
        if left_side_node.val != right_side_node.val:
            return False
        
        return self.dfs(left_side_node.left, right_side_node.right) and self.dfs(left_side_node.right, right_side_node.left)

    
            



    
    
