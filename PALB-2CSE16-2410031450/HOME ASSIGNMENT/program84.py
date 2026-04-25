'''Difference Check
Given an array arr[] of time strings in 24-hour clock format "HH:MM:SS", return
the minimum difference in seconds between any two time strings in the arr[].
The clock wraps around at midnight, so the time difference between "23:59:59" and
"00:00:00" is 1 second.'''
def min_time_difference(arr):
    times = []
    for t in arr:
        h, m, s = map(int, t.split(":"))
        total = h * 3600 + m * 60 + s
        times.append(total)
    times.sort()
    min_diff = float('inf')
    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i-1])
    seconds_in_day = 24 * 3600
    circular_diff = seconds_in_day - (times[-1] - times[0])
    return min(min_diff, circular_diff)
# Example
arr = ["23:59:59", "00:00:00", "12:30:15"]
print(min_time_difference(arr))  # Output: 1