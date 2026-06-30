class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            unique = set()
            for num in row:
                if num != ".":
                    if int(num) in unique:
                        print(f"in row iteration, the num is {num}")
                        return False 
                    unique.add(int(num))



        for i in range(9):
            unique = {}
            for j in range(9):
                if board[j][i] != ".":
                    if unique.get(int(board[j][i]), 0):
                        print(f"in row iteration, the num is {int(board[j][i])}")
                        return False 
                    unique[int(board[j][i])] = 1


        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3)*3 + i
                    col = (square % 3)*3 + j
                    # print(row, col)

                    if board[row][col] != ".":
                        # print(board[row][col])
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])




        return True