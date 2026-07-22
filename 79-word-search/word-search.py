class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def solve(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= n or j < 0 or j >=m:
                return False
            
            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = (solve(i+1,j,k+1) or
                    solve(i-1,j,k+1) or
                    solve(i,j+1,k+1) or
                    solve(i,j-1,k+1)
            )

            board[i][j] = temp

            return found

        for i in range(n):
            for j in range(m):
                if solve(i,j,0):
                    return True

        return False

        

        
        

        