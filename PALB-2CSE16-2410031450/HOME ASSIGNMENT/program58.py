'''You are given an array arr[]. The task is to determine whether the array contains a 132
pattern, i.e., three indices i, j and k such that i < j < k , arr[i] < arr[j] >
arr[k] and arr[i] < arr[k].
Return true if such a triplet exists, otherwise return false.'''
def find132pattern(arr):
    stack = []
    third = float('-inf') 
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < third:
            return True
        while stack and stack[-1] < arr[i]:
            third = stack.pop()
        stack.append(arr[i])
    return False
# Example 1
arr1 = [4, 7, 11, 5, 13, 2]
print(find132pattern(arr1))  # Output: True
# Example 2
arr2 = [11, 11, 12, 9]
print(find132pattern(arr2))  # Output: False