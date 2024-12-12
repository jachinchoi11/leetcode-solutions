class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # go through the array until you see first letter and then run a dfs and see if you're able to get through to very end
        # keep track of this using a global variable and then you can note it down somewhere 

        rows, cols = len(board), len(board[0])
        visited = set()
        self.found = False

        def dfs(row, col, index, currVisited):
            if index == len(word):
                self.found = True
                return
            if row < 0 or col < 0 or row == rows or col == cols or (row, col) in currVisited or board[row][col] != word[index]:
                return
            currVisited.add((row, col))
            dfs(row + 1, col, index + 1, currVisited)
            dfs(row - 1, col, index + 1, currVisited)
            dfs(row, col + 1, index + 1, currVisited)
            dfs(row, col - 1, index + 1, currVisited)
            currVisited.remove((row, col))
        
        currVisited = set()

        for row in range(rows):
            for col in range(cols):
                if board[row][col] != word[0] or (row, col) in visited:
                    continue
                else:
                    dfs(row, col, 0, currVisited)
                    visited.add((row, col))
            if self.found:
                return True
        return False
