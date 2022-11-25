#adding numbers unti you come up with a single digit
"""
e.g n='9874' , k=4 then n will be '9874987498749874'
sum of the new string until you find a base single
"""

def check(n):
    if int(n)< 10:
        return n
    
    return check(sum([int(x) for x in str(n)]))
    
    

def superDigit(n, k):
    
    return check(k * check(int(n)))