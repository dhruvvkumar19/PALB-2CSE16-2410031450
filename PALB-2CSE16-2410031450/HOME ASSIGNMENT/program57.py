'''You are given an integer array arr[ ]. Your task is to count the number of subarrays
where the first element is the minimum element of that subarray.'''
def count_valid_subarrays(arr):
    n = len(arr)
    stack = []
    nse = [n] * n 
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            nse[idx] = i
        stack.append(i)
    count = 0
    for i in range(n):
        count += (nse[i] - i)
    return count
# Example 1
arr1 = [1, 2, 1]
print(count_valid_subarrays(arr1))  # Output: 5
# Example 2
arr2 = [1, 3, 5, 2]
print(count_valid_subarrays(arr2))  # Output: 8