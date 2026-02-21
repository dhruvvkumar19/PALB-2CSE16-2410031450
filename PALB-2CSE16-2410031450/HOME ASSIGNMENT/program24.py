'''Given an array arr and a number k. One can apply a swap operation on the array any
number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find
the minimum number of swaps required to bring all the numbers less than or equal
to k together, i.e. make them a contiguous subarray.'''
def min_swaps(arr, k):
    n = len(arr)
    good = 0
    for num in arr:
        if num <= k:
            good += 1
    bad = 0
    for i in range(good):
        if arr[i] > k:
            bad += 1
    min_swaps = bad
    i = 0
    j = good
    while j < n:
        if arr[i] > k:
            bad -= 1
        if arr[j] > k:
            bad += 1
        min_swaps = min(min_swaps, bad)
        i += 1
        j += 1
    return min_swaps
print(min_swaps([2, 1, 5, 6, 3], 3))       
print(min_swaps([2, 7, 9, 5, 8, 7, 4], 6))  
print(min_swaps([2, 4, 5, 3, 6, 1, 8], 6))  