class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        if not root:
            return []

        def isLeaf(node):
            return node.left is None and node.right is None

        # Collect left boundary (excluding leaves)
        def getLeftBoundary(node):
            boundary = []
            while node:
                if not isLeaf(node):
                    boundary.append(node.val)
                node = node.left if node.left else node.right
            return boundary

        # Collect right boundary (in reverse order, excluding leaves)
        def getRightBoundary(node):
            boundary = []
            while node:
                if not isLeaf(node):
                    boundary.append(node.val)
                node = node.right if node.right else node.left
            return boundary[::-1]

        # Collect all leaf nodes using DFS to preserve left-to-right order
        def getLeaves(node, leaves):
            if not node:
                return
            if isLeaf(node):
                leaves.append(node.val)
            getLeaves(node.left, leaves)
            getLeaves(node.right, leaves)

        # Root node
        boundary = [root.val] if not isLeaf(root) else []

        # Collect and append boundaries and leaves in the correct order
        left_boundary = getLeftBoundary(root.left)
        leaves = []
        getLeaves(root, leaves)
        right_boundary = getRightBoundary(root.right)

        # Concatenate left boundary, leaves, and reversed right boundary
        boundary += left_boundary + leaves + right_boundary
        return boundary
