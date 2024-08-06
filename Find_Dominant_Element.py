# For this mock interview, you will go through four phases: Prompt, Plan, Code, & Test.
# Prompt: Understand the problem.
# Plan: Outline your approach.
# Code: Implement your solution.
# Test: Verify your solution works.

# Here is the problem that you will be solving:
# Imagine you have a list of numbers, referred to as 'nums', with a total length of 'n'.
# Your task is to identify the dominant element in this list.
# The dominant element is defined as the one that appears more than half the time (n / 2) in the list.
# It is guaranteed that such an element exists in the list.
 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
 
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# - The length of 'nums' is equal to 'n'.
# - 'n' ranges from 1 to 50,000.
# - Each element in 'nums' can be any integer between -1,000,000,000 and 1,000,000,000.

# Plan: I will use a dictionary to store the count of each element in the list.
# #I will iterate through the list and increment the count of each element in the dictionary.
# #I will then iterate through the dictionary and return the element that has a count greater than n/2.

def find_dominant_element(nums):
    count_dict = {}
    n = len(nums)
    
    # Count the occurrences of each element
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the dominant element
    for num, count in count_dict.items():
        if count > n / 2:
            return num
        
# Test cases
print(find_dominant_element([3,2,3])) # 3
print(find_dominant_element([2,2,1,1,1,2,2])) # 2
print(find_dominant_element([1,1,1,2,2,2,2])) # 2

# Time complexity: O(n)
# Space complexity: O(n)
