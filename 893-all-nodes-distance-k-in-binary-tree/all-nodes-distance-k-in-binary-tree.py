# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
    # so first thing we need to do is to be able to find the target node 
        # and find how far away soemthing this 

    # we can create an adjacency list that allows undirected travle throughout the tree 
        # so basically it can refer back to the parent pointers, and that way everything will be connected 
    
    # traversing through the adjcencey list from our target --> and going k times 
        adj_list = defaultdict(list)
        self.create_adj_list(root, None, adj_list)
        visited = set()

        
        queue = deque([target.val])
        visited.add(target.val)

        while queue and k > 0:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                for neighbor in adj_list[curr_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            k -= 1
        return list(queue)
        
    
        



    
    def create_adj_list(self, node, parent, adj_list):
        # we are creating the adjacency list
        if not node:
            return
        
        if parent:
            adj_list[node.val].append(parent.val)
            adj_list[parent.val].append(node.val)
        
        self.create_adj_list(node.left, node, adj_list)
        self.create_adj_list(node.right, node, adj_list)



    

        


