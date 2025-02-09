# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        # ok so basically its root + left boundar of root (left side view)

        # what if we have a thing for find left boundary
        # find right boundary 
        # then we could just pop a bfs where we disregard the first right child, 
        # so we would essentially pass in root.left node and then give it 0 --> cause it will look fro the first index at each level for boundary 

        # and then for the right boundary we will pass root.right node and then give it -1, so it can look for the last one to be added which would be right bounary 
        # and then just appedn it to our answer in reversed order 

        def isLeafNode(node):
            if not node.left and not node.right:
                return True
            return False
        
        boundary_values = [root.val]
        rightBoundary = []
        
        def getLeft(curr_node):
            if not curr_node:
                return
            if not isLeafNode(curr_node):
                boundary_values.append(curr_node.val)
            getLeft(curr_node.left) if curr_node.left else getLeft(curr_node.right)
        
        def getRight(curr_node):
            if not curr_node:
                return
            if not isLeafNode(curr_node):
                rightBoundary.append(curr_node.val)
            getRight(curr_node.right) if curr_node.right else getRight(curr_node.left)

        def getLeaves(curr_node):
            if not curr_node:
                return
            if isLeafNode(curr_node) and curr_node != root:
                boundary_values.append(curr_node.val)
            getLeaves(curr_node.left)
            getLeaves(curr_node.right)
        
        if root.left:
            getLeft(root.left)

        getLeaves(root)
        if root.right:
            getRight(root.right)

        boundary_values.extend(reversed(rightBoundary))

        return boundary_values
