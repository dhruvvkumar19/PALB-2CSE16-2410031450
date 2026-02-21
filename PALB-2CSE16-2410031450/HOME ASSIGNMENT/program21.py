'''Given an array arr[] of positive integers, where each value represents the number of
chocolates in a packet. Each packet can have a variable number of chocolates. There
are m students, the task is to distribute chocolate packets among m students such that -
i. Each student gets exactly one packet.
ii. The difference between maximum number of chocolates given to a student and
minimum number of chocolates given to a student is minimum and return that
minimum possible difference.'''
def chocolate_distribution(arr, m):
    if m > len(arr):
        return -1
    arr.sort()
    min_diff = 999999999
    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff
arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(chocolate_distribution(arr, m))