"""
Anagram is finding out if iftwo strings have same frequency i.e if one
string its characters can be interchanged to form the other string
e.g garden and danger,
"""
n='garden'
m='danger'

#using sorting
def sort_anagram(n,m):
    if len(n) == len(m):
        if sorted(n) == sorted(m):
            return True
        return False 
        
    return False

#using hash table
occur1 = {}
occur2 = {}

def hash_table_anagram(n,m):
    if len(n) != len(m):
        return False
    for char in n:
        if char in occur1:
            occur1[char] += 1
        occur1[char] = 1
    for char in m:
        if char in occur2:
            occur2[char] += 1
        occur2[char] = 1
 
    for x in occur1:
        return x in occur2 and occur1[x] == occur2[x]

#using the collection module, this procedure is a short form of the hash table
from collections import Counter
def counter_anagram(n,m):
    if len(n) != len(m):
        return False
    return Counter(n) == Counter(m)

# print(counter_anagram(n,m))



