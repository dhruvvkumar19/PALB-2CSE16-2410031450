def rotate_clockwise(arr):
    if len(arr) == 0:
        return arr
    
    last = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr

arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

rotate_clockwise(arr)
print("After rotation:", arr)