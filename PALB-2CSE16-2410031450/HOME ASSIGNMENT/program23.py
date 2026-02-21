'''Given an array and a range a, b. The task is to partition the array around the range
such that the array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to
return the modified array.
Note: The generated output is true if you modify the given array successfully.
Otherwise false.'''
def three_way_partition(arr, a, b):
    start = 0
    end = len(arr) - 1
    i = 0
    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1   
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1  
        else:
            i += 1 
    return arr
arr = [1, 2, 3, 3, 4]
a = 1
b = 2
print(three_way_partition(arr, a, b))