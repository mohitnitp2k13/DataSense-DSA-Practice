# Question 1: Sort Tuples by Sum of Elements
# Title: Sort Tuples by Sum.

# Description:
# You are given a list of tuples, where each tuple contains exactly two integers. Sort this list in ascending order based on the sum of the integers in each tuple.

# Input: [(3, 1), (2, 2), (5, -1), (0, 0)]
# Output: [(0, 0), (3, 1), (2, 2), (5, -1)]

# Input: [(7, 3), (1, 2), (4, 5), (0, 1)]
# Output: [(0, 1), (1, 2), (4, 5), (7, 3)]

# Input: [(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]
# Output: [(1, 1), (2, 0), (8, -3), (3, 2), (5, 5)]

def sort_by_tuple_sum(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
    op_list = sorted(lst, key= lambda x:x[0]+x[1])
    return op_list


Input = [(3, 1), (2, 2), (5, -1), (0, 0)]
op = sort_by_tuple_sum(Input)
print(op)

