'''You are given an array arr[ ], where arr[i] represents the height of the ith person standing
in a line.
A person i can see another person j if:
• height[j] < height[i],
• There is no person k standing between them such that height[k] ≥ height[i].
Each person can see in both directions (front and back).
Your task is to find the maximum number of people that any person can see
(including themselves).'''
def max_people_seen(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    stack = []
    for i in range(n):
        count = 0
        while stack and arr[stack[-1]] < arr[i]:
            count += 1
            stack.pop()
        if stack:
            count += 1
        left[i] = count
        stack.append(i)
    stack.clear()
    for i in range(n - 1, -1, -1):
        count = 0
        while stack and arr[stack[-1]] < arr[i]:
            count += 1
            stack.pop()
        if stack:
            count += 1
        right[i] = count
        stack.append(i)
    max_seen = 0
    for i in range(n):
        max_seen = max(max_seen, left[i] + right[i] + 1)
    return max_seen
# Example 1
arr1 = [6, 2, 5, 4, 5, 1, 6]
print(max_people_seen(arr1))  # Output: 5
# Example 2
arr2 = [1, 3, 6, 4]
print(max_people_seen(arr2))  # Output: 3