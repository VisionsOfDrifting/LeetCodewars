"""Problem:
   Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
   The distance between two adjacent cells is 1. 
   Example 1:
   Input:
   0 0 0
   0 1 0
   0 0 0
   Output:
   0 0 0
   0 1 0
   0 0 0
   Example 2:
   Input:
   0 0 0
   0 1 0
   1 1 1
   Output:
   0 0 0
   0 1 0
   1 2 1
   Note:
   The number of elements of the given matrix will not exceed 10,000.
   There are at least one 0 in the given matrix.
   The cells are adjacent in only four directions: up, down, left and right.
"""

def nearestZero(matrix):
   m, n = len(matrix), len(matrix and matrix[0])
   for i in range(m):
      for j in range(n):
         if matrix[i][j] != 0:
            matrix[i][j] = float("inf")
            if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
               print("i",matrix[i][j],matrix[i - 1][j],"+ 1")
               matrix[i][j] = matrix[i - 1][j] + 1
            if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
               print("j",matrix[i][j],matrix[i][j - 1],"+ 1")
               matrix[i][j] = matrix[i][j - 1] + 1
         print(i,j)
         print(matrix)
   for i in range(m - 1, -1, -1):
      for j in range(n - 1, -1, -1):
         if matrix[i][j] != 0:
            if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
               print("i",matrix[i][j],matrix[i + 1][j],"+ 1")
               matrix[i][j] = matrix[i + 1][j] + 1
            if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
               print("j",matrix[i][j],matrix[i][j + 1],"+ 1")
               matrix[i][j] = matrix[i][j + 1] + 1
         print(i,j)
         print(matrix)
   return matrix

#matrix = [[0,1,1],[1,1,1],[1,1,1]]
matrix = [[1,1,1],[1,1,1],[1,1,0]]
#matrix = [[0,0,0],[0,1,0],[1,1,1]]
print(matrix)
print(nearestZero(matrix))

#The trick in this one is to set all non-zero values to 'inf' thats why the comparison works
#First pass, top left to bottom right, look at the neighbors above and to the right
#Second pass, bottom right to top left, look at the neighbors below and to the left