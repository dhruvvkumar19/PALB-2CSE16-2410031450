'''Given two arrays a[] and b[], your task is to determine whether b[] is a subset
of a[].'''
def is_subset(a, b):
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    return True
print(is_subset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))  
print(is_subset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))              
print(is_subset([10, 5, 2, 23, 19], [19, 5, 3]))                 