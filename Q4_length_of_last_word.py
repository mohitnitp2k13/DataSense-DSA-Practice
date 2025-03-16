# Question 2: Length of Last Word
# Title: Length of Last Word

# Description:
# You are given a string s that contains words and spaces. Your task is to find the length of the last word in the sentence.


# Example:

# Input: 
s = "Learn Python"
# Output: 6
# Explanation: The last word is "Python", which has 6 letters.

# Input:
# s = "   coding is fun   "
# Output: 3
# Explanation: The last word is "fun", which has 3 letters.

# Input: 
# s = " fly me   to the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

def length_of_last_word(s: str) -> int:
    s = s.strip()
    lst_strgs = s.split(" ")
    return len(lst_strgs[-1])
    
op = length_of_last_word(s)
print(op)