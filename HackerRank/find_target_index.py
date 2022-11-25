"""
Find the start and end index of a targeted number in a sorted list e.g
[1,2,2,2,3,3,5] , target of 3 will be the start index of 3 which is 4, end is 5 thus
[4,5]. if number is not in the array return [-1,-1]
"""
list_num =  [2,4,5,5,5,5,5,7,9,9]
target = 5

def target_index_finder(list_num, target):
    index_all = []
    if target in list_num:
        for index, num in enumerate(list_num):
            if target == num:
                index_all.append(index)
        return [index_all[0],index_all[-1]]
    return [-1,-1]
        
#getting the start index of the target and last target occurance in a list
def first_last(list_num, target):
        for index, num in enumerate(list_num):
            if num == target:
                start_index = index
                while index+1 < len(list_num) and list_num[index+1] == target:
                    index += 1
                return [start_index, index]
        return [-1,-1]


