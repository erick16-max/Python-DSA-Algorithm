"""
finding the Kth largest number in a list of intergers e.g
arr = [4,2,9,7,5,6,7,1,3], find the 4th largest number which will be 6
"""

list_num = [4,2,9,7,5,6,7,1,3]
k = 4
def kth_number(list_num, k):
    list_num.sort(reverse=True)
    return list_num[k-1]

print(kth_number(list_num, k))