'''You are given an integer array arr[ ]. For every element in the array, your task is to
determine its Previous Smaller Element (PSE).
The Previous Smaller Element (PSE) of an element x is the first element that appears to
the left of x in the array and is strictly smaller than x.'''
def previous_smaller(arr):
    stack = []
    result = []
    for x in arr:
        while stack and stack[-1] >= x:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(x)
    return result
# Example 1
arr1 = [1, 6, 2]
print(previous_smaller(arr1))  # Output: [-1, 1, 1]
# Example 2
arr2 = [1, 5, 0, 3, 4, 5]
print(previous_smaller(arr2))  # Output: [-1, 1, -1, 0, 3, 4]