# Question 2: Filter Strings Based on Criteria
# Title: Filter Strings by Length and Vowel Count

# Description:
# You are given a list of strings and two integers, k and m. Return a new list containing only those strings that satisfy both of the following conditions:
# The length of the string is greater than or equal to k.
# The string contains at least m vowels (vowels are 'a', 'e', 'i', 'o', 'u').
# The output should maintain the original order of appearance in the input list.

Input = ["apple", "hi", "world", "yes", "python"]
k = 4
m = 2
# Output: ["apple"]

Input = ["education", "science", "art", "mathematics"]
k = 5
m = 3
# Output: ["education", "science", "mathematics"]

def filter_strings(lst: list[str], k: int, m: int) -> list[str]:
    op_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for str1 in lst:
        count = 0
        # unique_letters = set(str1)
        count_vowels = sum(map(lambda x :1 if x in vowels else 0, str1))
        
        if len(str1) >= k and count_vowels >= m:
            op_list.append(str1)
            
    return op_list

op = filter_strings(Input,k,m)
print(op)

