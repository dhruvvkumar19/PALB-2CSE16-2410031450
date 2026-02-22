'''Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and
columns is always odd. Return the median of the matrix.'''
def matrixMedian(matrix):
    arr = []
    for row in matrix:
        arr.extend(row)  
    arr.sort()  
    return arr[len(arr)//2]
matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(matrixMedian(matrix))