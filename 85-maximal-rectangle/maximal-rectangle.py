from collections import deque

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def calculate_area(rows):
            n = len(rows)

            # Find previous smaller element
            stack = deque()
            prev_smaller = [-1] * n
            for i in range(n-1,-1,-1):
                while stack and rows[i] < rows[stack[-1]]:
                    prev_smaller[stack[-1]] = i
                    stack.pop()
                stack.append(i)

            # Find next smaller element
            next_smaller = [n] * n
            stack = deque()
            for i in range(n):
                while stack and rows[i] < rows[stack[-1]]:
                    next_smaller[stack[-1]] = i
                    stack.pop()
                stack.append(i)

            # Find max area per row 
            max_area_per_row = 0
            for i in range(n):
                area = rows[i] * (next_smaller[i] - prev_smaller[i] - 1)
                max_area_per_row = max(max_area_per_row, area)

            return max_area_per_row


        row = len(matrix)
        column = len(matrix[0])

        # Type Conversion str to int
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1

        # Main Calculation  
        for i in range(1, row):
            for j in range(column):
                if matrix[i][j] > 0:
                    if matrix[i-1][j] > 0:
                        matrix[i][j] = matrix[i-1][j] + 1

        # Final Max Area after comparing all the max area per row 
        max_area = 0
        for i in range(row-1,-1,-1):
            max_area_perrow = calculate_area(matrix[i])
            max_area = max(max_area ,max_area_perrow)

        return max_area





                





                



        