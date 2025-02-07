# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        # in this case, you can technically easily do a dfs here at every path

        def dfs(curr_node, pointer):
            if not curr_node:
                return False
            
            if curr_node.val != pointer.val:
                return False
            else:
                if pointer.next == None:
                    return True
                pointer = pointer.next

            return dfs(curr_node.left, pointer) or dfs(curr_node.right, pointer)

        if not head:
            return True
        if not root:
            return False
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right) or dfs(root, head)