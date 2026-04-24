'''Given an array arr[], find the minimum number of operations required to make the
sum of its elements less than or equal to half of the original sum. In one operation, you
may replace any element with half of its value (with floating-point precision).'''
import heapq
def min_operations(arr):
    total = sum(arr)
    target = total / 2
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    operations = 0
    current_sum = total
    while current_sum > target:
        largest = -heapq.heappop(max_heap)
        half = largest / 2
        current_sum -= half
        heapq.heappush(max_heap, -half)
        operations += 1
    return operations
print(min_operations([8,6,2]))  # Output: 3
print(min_operations([9,1,2]))  # Output: 2