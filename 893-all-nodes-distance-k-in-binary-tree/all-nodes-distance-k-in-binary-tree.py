# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # create a graph for the problem and make sure to get the parent pointer 
        # we want to have a visited set, as we don't want to add things that we've already observed 
        # our answer will be the answers left in the queue
        # we put the target node in the queue at first and do the bfs iterate k -= 1
        # while queue and the k > 0

        graph = defaultdict(list)
        self.create_Graph(root, None, graph)
        return self.find_k_Distance_Away(graph, target.val, k)

    def create_Graph(self, node, parent, graph):
        # maps the node.values to the nodes
        if not node:
            return
        
        if parent:
            graph[node.val].append(parent.val)
        if node.right:
            graph[node.val].append(node.right.val)
        if node.left:
            graph[node.val].append(node.left.val)
        
        self.create_Graph(node.right, node, graph)
        self.create_Graph(node.left, node, graph)
    
    def find_k_Distance_Away(self, graph, target, k):

        queue = deque()
        queue.append(target)
        visited = set()

        print(queue)
        while queue and k > 0:
            for _ in range(len(queue)):
                curr_node_val = queue.popleft()
                for neighbor in graph[curr_node_val]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                visited.add(curr_node_val)
            k -= 1

        return list(queue)


    
        