"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # clone_graph -- the node given has valie = 1 and index 1 
        # so i think the way to approach this is to create nodes based off thier nodes 
        if not node:
            return None
        
        clone_nodes = {}

        clone_nodes[node.val] = Node(node.val)
        queue = deque([node])

        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor.val not in clone_nodes:
                    queue.append((neighbor))
                    clone_nodes[neighbor.val] = Node(neighbor.val)
                clone_neighbor = clone_nodes[neighbor.val]
                current_clone_neighbors = clone_nodes[curr_node.val].neighbors
                current_clone_neighbors.append(clone_neighbor)
            
        return clone_nodes[1]
             
        
        





        


