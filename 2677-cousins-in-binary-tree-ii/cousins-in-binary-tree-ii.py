# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # how are we going to replace the cousins, i think doing a bfs of some sort 
        
        # the idea is that we have to be able to distinguish what's part of it and what's not
        # and we can do that using the index of the parent -->

        # we'll set up a current hashmap and get the total_sum
        # that will group the index of the parent to the total_sum, we will then figure out what the value should be 
        # then we can assign the values the total_sum - the hashmap[curr_index]

        group_map = defaultdict(int)

        queue = deque()
        queue.append((root, -1))

        while queue:
            total_sum = 0
            for _ in range(len(queue)):
                curr_node, parent_node = queue.popleft()
                total_sum += curr_node.val
                group_map[parent_node] += curr_node.val
                queue.append((curr_node, parent_node))

            for _ in range(len(queue)):

                curr_node, parent_node = queue.popleft()
                curr_node.val = total_sum - group_map[parent_node]
                if curr_node.left:
                    queue.append((curr_node.left, curr_node))
                if curr_node.right:
                    queue.append((curr_node.right, curr_node))
        
        return root




