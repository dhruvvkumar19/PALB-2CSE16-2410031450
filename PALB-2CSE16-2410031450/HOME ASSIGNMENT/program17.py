'''Given three sorted arrays in non-decreasing order, print all common elements
in non-decreasing order across these arrays. If there are no such elements return
an empty array. In this case, the output will be -1.
Note: can you handle the duplicates without using any additional Data Structure?'''
def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    result = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return result if result else [-1]
print(common_elements(
    [1, 5, 10, 20, 40, 80],
    [6, 7, 20, 80, 100],
    [3, 4, 15, 20, 30, 70, 80, 120]
))
print(common_elements([1, 2, 3, 4, 5], [6, 7], [8, 9, 10]))
print(common_elements(
    [1, 1, 1, 2, 2, 2],
    [1, 1, 2, 2, 2],
    [1, 1, 1, 1, 2, 2, 2, 2]
))