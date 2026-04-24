'''Given two integers n and k, the task is to find all valid combinations of k numbers that
adds up to n based on the following conditions:
• Only numbers from the range [1, 9] used.
• Each number can only be used at most once.
Note: You can return the combinations in any order, the driver code will print them in
sorted order.'''
def combinationSum3(k, n):
    result = []
    def backtrack(start, path, total):
        # If valid combination found
        if len(path) == k and total == n:
            result.append(path[:])
            return
        if len(path) > k or total > n:
            return
        for i in range(start, 10):
            path.append(i)
            backtrack(i + 1, path, total + i)
            path.pop()  
    backtrack(1, [], 0)
    return result
# Example 1
print(combinationSum3(3, 9))
# Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
# Example 2
print(combinationSum3(3, 3))
# Output: []