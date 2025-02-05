# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # can you just do a bfs with a queue 
        # and then you have aqueue to get the answer
        # the left child you will append left to where you were 
        # and the right child you will append to the right
        # the only issue is with a queeu is that it might take O(n) time to get to that point and append 
        # instead we can look at it like almsot a number line with a x value 
        # i think maybe you can say the first value is 0, and +1 for right child, -1 for left child 

        # we can use a hashmap to kind of keep track of this and then maybe we can extract the values and sort it
        if not root:
            return []
        queue = deque()
        curr_x = 0
        x_value_tracker = defaultdict(list)
        queue.append((root, curr_x))
        minimum_index = float('inf')
        maximum_index = 0
        while queue:
            for _ in range(len(queue)):
                curr_node, curr_x = queue.popleft()
                if curr_node.left:
                    queue.append((curr_node.left, curr_x - 1))
                if curr_node.right:
                    queue.append((curr_node.right, curr_x + 1))
                x_value_tracker[curr_x].append(curr_node.val)
                minimum_index = min(minimum_index, curr_x)
                maximum_index = max(maximum_index, curr_x)

        ans = []

        for index in range(minimum_index, maximum_index + 1):
            ans.append(x_value_tracker[index])
        
        return ans