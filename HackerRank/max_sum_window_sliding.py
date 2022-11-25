"""
Given an array of integers of size "n", Our aim 
is to calculate the maximum sum of "k" consecutive elements in the array
"""

#using sliding window algorithm

list_num = [2,4,5,1,2,4,5,6]
k = 4

def find_max_sum(list_num, k):
    if len(list_num) < k:
        return -1
    max_sum = sum(list_num[:k])
    temp_sum = max_sum

    for index in range(len(list_num) - k):
        temp_sum = max_sum - list_num[index] + list_num[index + k]
        max_sum = max(max_sum, temp_sum)

    return max_sum

print(find_max_sum(list_num,k))
