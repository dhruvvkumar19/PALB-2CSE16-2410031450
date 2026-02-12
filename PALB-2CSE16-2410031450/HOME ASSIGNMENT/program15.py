'''Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in
sorted order without using any extra space. Modify a[] so that it contains the first n elements and
modify b[] so that it contains the last m elements.'''
import math
def next_gap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)
def merge_arrays(a, b):
    n = len(a)
    m = len(b)
    gap = next_gap(n + m)
    while gap > 0:
        i = 0
        while i + gap < n:
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
            i += 1
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1
        if j < m:
            j = 0
            while j + gap < m:
                if b[j] > b[j + gap]:
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1
        gap = next_gap(gap)
a = [2, 4, 7, 10]
b = [2, 3]
merge_arrays(a, b)
print("a =", a)
print("b =", b)
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
merge_arrays(a, b)
print("a =", a)
print("b =", b)