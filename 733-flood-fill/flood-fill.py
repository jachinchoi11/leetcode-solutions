class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = set()
        visit = []
        def dfs(row, col, visited):
            rows, cols = len(image), len(image[0])

            if min(row, col) < 0 or row == rows or col == cols or (row, col) in visited:
                return
            if len(visit) > 0:
                pastRow = visit[-1][0]
                pastCol = visit[-1][1]
                if image[row][col] != image[pastRow][pastCol]:
                    return

            visited.add((row, col))
            visit.append((row, col))

            dfs(row - 1, col, visited)
            dfs(row + 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)

        dfs(sr, sc, visited)
        for row, col in visit:
            image[row][col] = color
        return image