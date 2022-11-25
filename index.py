n = 2
m = 3

def square(number):
    return number ** 2

def sum(n,m):
    result = square(m) + square(n)
    return result

print(sum(n,m))