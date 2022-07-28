#Convert a matrix : [[1,2], [3,4], [5,6], [7,8]] into [[1,3,5,7], [2,4,6,8]]

matrix = [[1,2], [3,4], [5,6], [7,8]]
result = [[0,0,0,0], [0,0,0,0]]

#Picking one Element in each loop & replacing in result Matrix........
for i in range(len(matrix)):
   for j in range(len(matrix[0])):
       result[j][i] = matrix[i][j]
print(result)
