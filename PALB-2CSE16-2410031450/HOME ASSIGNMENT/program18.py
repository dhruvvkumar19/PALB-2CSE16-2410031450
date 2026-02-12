'''Given an integer n, find its factorial. Return a list of integers denoting the digits
that make up the factorial of n.'''
def factorial_digits(n):
    result = [1]
    for x in range(2, n + 1):
        carry = 0
        for i in range(len(result)):
            prod = result[i] * x + carry
            result[i] = prod % 10
            carry = prod // 10
        while carry:
            result.append(carry % 10)
            carry //= 10
    return result[::-1]
print(factorial_digits(5))   
print(factorial_digits(10)) 
print(factorial_digits(1))  