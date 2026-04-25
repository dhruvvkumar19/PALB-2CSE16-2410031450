'''Minimum number of swaps
You are given two binary strings s1 and s2 of equal length, and the task is to find
the minimum number of swaps required to make them identical. The only allowed
operation is swapping characters between the two strings (i.e., you can
swap s1[i] with s2[j], but not within the same string). If it is impossible to make the two
strings equal through such swaps, return -1.'''
def min_swaps(s1, s2):
    n = len(s1)
    total_ones = s1.count('1') + s2.count('1')
    if total_ones % 2 != 0:
        return -1
    mismatches = 0
    for i in range(n):
        if s1[i] != s2[i]:
            mismatches += 1
    return (mismatches + 1) // 2
# Example 1
print(min_swaps("1100", "1111"))  # Output: 1
# Example 2
print(min_swaps("00011", "11001"))  # Output: -1