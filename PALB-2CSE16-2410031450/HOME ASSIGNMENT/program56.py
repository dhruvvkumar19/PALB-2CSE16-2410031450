'''You are given an integer array arr[ ]. For every element in the array, your task is to
determine its Previous Greater Element (PGE).
The Previous Greater Element (PGE) of an element x is the first element that appears to
the left of x in the array and is strictly greater than x.'''
def previous_greater(arr):
    stack = []
    result = []
    for x in arr:
        while stack and stack[-1] <= x:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(x)
    return result
# Example 1
arr1 = [10, 4, 2, 20, 40, 12, 30]
print(previous_greater(arr1))  
# Output: [-1, 10, 4, -1, -1, 40, 40]
# Example 2
arr2 = [10, 20, 30, 40]
print(previous_greater(arr2))  
# Output: [-1, -1, -1, -1]