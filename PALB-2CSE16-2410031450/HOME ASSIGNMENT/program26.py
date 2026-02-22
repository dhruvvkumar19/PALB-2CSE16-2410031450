'''Given an array arr[] of integers, calculate the median.'''
def find_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2
print(find_median([90, 100, 78, 89, 67]))
print(find_median([56, 67, 30, 79]))
print(find_median([1, 2]))