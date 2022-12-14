import jovian
"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""


nums = [2,2]
target = 2
# Output: [3,4]

# nums = [5,7,7,8,8,10]
# target = 6
# Output: [-1,-1]

# nums = []
# target = 0
# Output: [-1,-1]

def find_first_index_of_target(nums, target):
 
    high = len(nums) - 1
    low = 0

    # if len(nums) == 0:
    #     return -1

    # if len(nums) == 1 and nums[0] == target:
    #     return len(nums)

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            if mid-1 >= 0 and nums[mid-1] == target:
                if (mid - 1) == 0:
                    return mid - 1
                return find_first_index_of_target(nums[:mid], target)
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid -1
    return -1

def searchRange(nums, target):
        
    start_index = find_first_index_of_target(nums,target)

    if start_index == -1:
        return [-1,-1]
    else:
        index = start_index
        while index+1 < len(nums) and nums[index+1] == target:
            index += 1
        return [start_index, index]
        
            
        

print(searchRange(nums, target))

jovian.commit(project='python-binary-search-leetcode-challenge', environment=None)

