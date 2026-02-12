'''Given an array arr[] denoting heights of n towers and a positive integer k.
For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers
after you have modified each tower.
You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by k for each tower. After the operation,
the resultant array should not contain any negative integers.'''
def get_min_diff(arr, k):
    n = len(arr)
    arr.sort()
    ans = arr[n-1] - arr[0]
    small = arr[0] + k
    big = arr[n-1] - k
    if small > big:
        small, big = big, small
    for i in range(1, n-1):
        subtract = arr[i] - k
        add = arr[i] + k
        if subtract >= small or add <= big:
            continue
        if big - subtract <= add - small:
            small = subtract
        else:
            big = add
    return min(ans, big - small)
print(get_min_diff([1, 5, 8, 10], 2))      # Output: 5
print(get_min_diff([3, 9, 12, 16, 20], 3)) # Output: 11