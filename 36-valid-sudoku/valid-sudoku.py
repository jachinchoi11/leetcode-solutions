class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board) , len(board[0])

        row_tracker = defaultdict(set)
        col_tracker = defaultdict(set)
        box_tracker = defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                    
                curr_num = board[row][col]

                if curr_num in row_tracker[row] or curr_num in col_tracker[col]:
                    return False
                
                row_tracker[row].add(curr_num)
                col_tracker[col].add(curr_num)

                if len(row_tracker[row]) == 9:
                    row_complete = True
                
                if len(col_tracker[col]) == 9:
                    col_complete = True

                box_key = ((row // 3, col // 3))

                if curr_num in box_tracker[box_key]:
                    return False
                box_tracker[box_key].add(curr_num)

                if len(box_tracker[box_key]) == 9:
                    box_complete = True
            
        return True 
        
        


