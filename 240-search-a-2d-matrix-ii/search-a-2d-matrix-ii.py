class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(0,rows,1):
            low = 0 
            high = columns - 1

            while low <= high:
                mid = (low + high) // 2

                if matrix[i][mid] == target:
                    return True
                
                elif matrix[i][mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1


        return False

