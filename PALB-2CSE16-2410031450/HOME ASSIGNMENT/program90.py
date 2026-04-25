'''Lexicographically Largest String After K Deletions
Given a string s consisting of lowercase English letters and an integer k, your task is to
remove exactly k characters from the string. The resulting string must be the largest
possible in lexicographical order, while maintain the relative order of the remaining
characters.'''
def largest_string_after_k_deletions(s, k):
    stack = []
    for ch in s:
        while stack and stack[-1] < ch and k > 0:
            stack.pop()
            k -= 1
        stack.append(ch)
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack)
# Examples
print(largest_string_after_k_deletions("abcde", 2))   # Output: cde
print(largest_string_after_k_deletions("cbacdcbc", 2)) # Output: cdcbc