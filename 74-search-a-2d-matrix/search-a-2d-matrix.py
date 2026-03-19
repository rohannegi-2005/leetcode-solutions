class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        for i in range(row):
            low = 0
            high = column - 1
            while low <= high:
                mid = (low + high) // 2

                if matrix[i][mid] == target:
                    return True

                elif matrix[i][mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

        return False

            


                

        