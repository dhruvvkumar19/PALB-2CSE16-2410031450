'''Sort by Frequency
Given a string s, the task is to arrange the string according to the frequency of each
character, in ascending order. If two elements have the same frequency, then they are
sorted in lexicographical order.'''
from collections import Counter
def sort_by_frequency(s):
    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
    result = ""
    for ch, count in sorted_chars:
        result += ch * count
    return result
# Examples
print(sort_by_frequency("tree"))   # Output: eert or eetr (depending order rule → here: eert)
print(sort_by_frequency("cccaaa")) # Output: aaaccc
print(sort_by_frequency("Aabb"))   # Output: bbAa