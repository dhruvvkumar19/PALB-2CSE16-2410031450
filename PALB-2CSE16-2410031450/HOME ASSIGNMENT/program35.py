'''Given an array of strings strs, group the anagrams together. You can return the answer
in any order.'''
def groupAnagrams(strs):
    d = {}
    for s in strs:
        key = str(sorted(s))
        d.setdefault(key, []).append(s)
    return list(d.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))