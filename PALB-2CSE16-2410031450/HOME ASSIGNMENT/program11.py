'''Given an integer array arr[] and an integer k, your task is to find and return the kth smallest
element in the given array.
Note: The kth smallest element is determined based on the sorted order of the array.'''
def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]

arr1 = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k1 = 4
print(kth_smallest(arr1, k1))
arr2 = [7, 10, 4, 3, 20, 15]
k2 = 3
print(kth_smallest(arr2, k2))