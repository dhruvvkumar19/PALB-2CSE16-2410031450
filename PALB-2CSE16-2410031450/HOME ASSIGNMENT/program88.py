'''Winner of an election
Given a lowercase string array arr[]. Each element in the array represents a vote cast
for a candidate. Return the name of the candidate who received the maximum number
of votes and the count of votes he received. In case of a tie between two or more
candidates, return the lexicographically smallest name.
Note: Return an array of strings, the winning candidate name as the first element and
the vote count as the second element (typecast the count to string).'''
from collections import Counter
def winner(arr):
    freq = Counter(arr)
    max_votes = 0
    winner_name = ""
    for name in sorted(freq):  
        if freq[name] > max_votes:
            max_votes = freq[name]
            winner_name = name
    return [winner_name, str(max_votes)]
# Example
arr = ["john", "john", "jack", "jack", "jack", "jill"]
print(winner(arr))  # Output: ['jack', '3']