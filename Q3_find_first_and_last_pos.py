# Question 1: Find First and Last Position of Element in Sorted Array
# Title: Find First and Last Position of Element in Sorted Array

# Description:
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If the target is not found in the array, return [-1, -1].


# Example:
# input: 
nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]

# Input: 
# nums = [5,7,7,8,8,10]
# target = 6
# Output: [-1,-1]

# Input: 
# nums = []
# target = 0
# Output: [-1,-1] 

def search_range(nums: list[int], target: int) -> list[int]:
    count_target = sum(map(lambda x:1 if x == target else 0, nums))
    try:
        idx = nums.index(target)
        # print(idx)
    except Exception as e:
        # print(e)
        idx = -1
    if idx == -1:
        return [-1,-1]
    if count_target > 1:
        return [idx, idx+1]
    else:
        return [idx, idx]

op = search_range(nums, target)
print(op)