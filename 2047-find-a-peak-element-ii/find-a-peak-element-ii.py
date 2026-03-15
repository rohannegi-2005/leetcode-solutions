class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        for i in range(rows):
            for j in range(cols):

                if (
                    (i == 0 or mat[i][j] > mat[i-1][j]) and
                    (i == rows-1 or mat[i][j] > mat[i+1][j]) and
                    (j == 0 or mat[i][j] > mat[i][j-1]) and
                    (j == cols-1 or mat[i][j] > mat[i][j+1])
                ):
                    return [i, j]
        