# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque()

        queue.append(root)
        if not root:
            return []
        res = []
        while queue:
            currMax = float('-inf')
            for i in range(len(queue)):
                curr = queue.popleft()
                currMax = max(currMax, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(currMax)
        
        return res

                

