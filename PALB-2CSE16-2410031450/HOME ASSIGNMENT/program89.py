'''Check if Permutation is Substring
Given two strings txt and pat having lowercase letters, the task is to check if any
permutation of pat is a substring of txt.'''
from collections import Counter

def check_permutation(txt, pat):
    n, m = len(txt), len(pat)
    if m > n:
        return False
    pat_count = Counter(pat)
    window_count = Counter(txt[:m])
    if window_count == pat_count:
        return True
    for i in range(m, n):
        # Add new character
        window_count[txt[i]] += 1
        window_count[txt[i - m]] -= 1
        if window_count[txt[i - m]] == 0:
            del window_count[txt[i - m]]
        if window_count == pat_count:
            return True
    return False
# Examples
print(check_permutation("oidbcaf", "abc"))  # True ("bca")
print(check_permutation("odicf", "dc"))     # False
print(check_permutation("bcdxabcdy", "bcdyabcdx"))  # True