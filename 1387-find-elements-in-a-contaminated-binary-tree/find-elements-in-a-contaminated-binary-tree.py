# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.hashset = set()
        queue = deque()
        queue.append((root, 0, 2))

        while queue:
            current_node, parent_val, l_or_r = queue.popleft()
            if l_or_r == 0:
                current_node.val = parent_val * 2 + 1
            elif l_or_r == 1:
                current_node.val = parent_val * 2 + 2
            
            if current_node.left:
                queue.append((current_node.left, current_node.val, 0))
            if current_node.right:
                queue.append((current_node.right, current_node.val, 1))
            self.hashset.add(current_node.val)
    
    def find(self, target: int) -> bool:
        return True if target in self.hashset else False



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)