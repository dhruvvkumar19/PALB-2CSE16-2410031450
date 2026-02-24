'''Given a collection of candidate numbers (candidates) and a target number (target), find
all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.'''
def combinationSum2(candidates, target):
    candidates.sort()  
    result = []
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            current.append(candidates[i])
            backtrack(i + 1, current, remaining - candidates[i])
            current.pop()  
    backtrack(0, [], target)
    return result
print(combinationSum2([10,1,2,7,6,1,5], 8))
print(combinationSum2([2,5,2,1,2], 5))