'''You are given an array arr[] of size n , where arr[i] denotes the range of working hours
a person at position i can cover.
• If arr[i] ≠ -1, the person at index i can work and cover the time interval [i -
arr[i], i + arr[i]].
• If arr[i] = -1, the person is unavailable and cannot cover any time.
The task is to find the minimum number of people required to cover the entire working
day from 0 to n - 1. If it is not possible to fully cover the day, return -1.'''
def min_people(arr):
    n = len(arr)
    intervals = []
    for i in range(n):
        if arr[i] != -1:
            left = max(0, i - arr[i])
            right = min(n - 1, i + arr[i])
            intervals.append((left, right))
    intervals.sort()
    count = 0
    i = 0
    current_end = 0
    farthest = 0
    while current_end < n:
        found = False
        while i < len(intervals) and intervals[i][0] <= current_end:
            farthest = max(farthest, intervals[i][1])
            i += 1
            found = True
        if not found:
            return -1
        count += 1
        current_end = farthest + 1
        if farthest >= n - 1:
            return count
    return -1
arr = [1, 0, 2, -1, 1, 0]

result = min_people(arr)
print("Minimum people required:", result)