# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # queue will have a tuple of the root.val as well as the index 
        queue = deque()
        maxWidth = 0
        if root:
            queue.append((root, 0))
        
        while len(queue) > 0:
            currRes = []
            for _ in range(len(queue)):
                currNode, index = queue.popleft()
                # essentially you are saving the indexes and the currentNodes 
                # so you can see the max at each level
                if currNode.left:
                    queue.append((currNode.left, 2 * index + 1))
                if currNode.right:
                    queue.append((currNode.right, 2 * index + 2))
                currRes.append(index)    
            maxWidth = max(maxWidth, currRes[-1] - currRes[0] + 1)

        return maxWidth

                       


