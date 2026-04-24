'''Given a matrix a of size n*m which represents a park, there is some construction work
needs to be done. You are also given q queries each query contains two
numbers R and C, For every query we need to construct a footpath in the Rth row
and Cth column, there is a cost of this construction, after the construction this path will
divide the park into sections, and the cost of the construction is
the sum of minimum value present in all the sections. You are asked to find this cost
for all the queries.'''
def get_min(a, r1, c1, r2, c2):
    if r1 > r2 or c1 > c2:
        return None
    mn = float('inf')
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            mn = min(mn, a[i][j])
    return mn
def solve(a, queries):
    n = len(a)
    m = len(a[0])
    results = []
    for R, C in queries:
        # convert to 0-based
        R -= 1
        C -= 1
        total = 0
        sections = [
            (0, 0, R-1, C-1),     # top-left
            (0, C+1, R-1, m-1),   # top-right
            (R+1, 0, n-1, C-1),   # bottom-left
            (R+1, C+1, n-1, m-1)  # bottom-right
        ]
        for r1, c1, r2, c2 in sections:
            val = get_min(a, r1, c1, r2, c2)
            if val is not None:
                total += val
        results.append(total)
    return results
# Example 1
a1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
queries1 = [(2,2)]
print(solve(a1, queries1))  # Output: [20]
# Example 2
a2 = [
    [1,2,3,4],
    [5,6,7,8],
    [1,2,3,4]
]
queries2 = [(3,4)]
print(solve(a2, queries2))  # Output: [1]