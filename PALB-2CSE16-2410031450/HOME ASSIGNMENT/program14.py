'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n]
inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra
space.'''
def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
print(find_duplicate([1,3,4,2,2]))  
print(find_duplicate([3,1,3,4,2]))  
print(find_duplicate([3,3,3,3,3]))  
