'''You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the
array is sorted in non-decreasing order. Your task is to find and return the index of the
first row that contains the maximum number of 1s. If no such row exists, return -1.'''
def rowWithMax1s(arr):
    n = len(arr)
    m = len(arr[0])
    max_ones = 0
    result = -1
    for i in range(n):
        left, right = 0, m - 1
        first_one = m
        while left <= right:
            mid = (left + right) // 2
            if arr[i][mid] == 1:
                first_one = mid
                right = mid - 1
            else:
                left = mid + 1
        ones_count = m - first_one
        if ones_count > max_ones:
            max_ones = ones_count
            result = i
    return result
arr = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
print(rowWithMax1s(arr))