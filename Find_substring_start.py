# Imagine you have a long piece of text ('haystack') and you are looking for a specific smaller string ('needle') within it.
# Your task is to determine where in the text the smaller string first shows up.
# You should output the starting position of the first occurrence of the 'needle' in the 'haystack'.
# Should the 'needle' not be found within the 'haystack', your program must return -1, indicating its absence.
 
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: The substring "sad" is first found at the start of the "haystack", thus the output is 0.
 
# Example 2:
# Input: haystack = "helloworld", needle = "123"
# Output: -1
# Explanation: Since "123" is not present in "helloworld", we return -1.
 
# Constraints:
# The length of both 'haystack' and 'needle' will be between 1 and 10^4, inclusive.
# Both 'haystack' and 'needle' will contain only lowercase English letters.

def findSubstringStart(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    
    if needle_len == 0:
        return 0
    
    for i in range(haystack_len - needle_len + 1):
        j = 0
        while j < needle_len and haystack[i + j] == needle[j]:
            j += 1
        if j == needle_len:
            return i
    
    return -1

# Example usage:
print(findSubstringStart("sadbutsad", "sad"))  # Output: 0
print(findSubstringStart("helloworld", "123"))  # Output: -1

# Time complexity: O(n*m)
# Space complexity: O(1)

# The time complexity of this solution is O(n*m), where n is the length of the 'haystack' and m is the length of the 'needle'.
# This is because we are iterating through the 'haystack' and comparing each character with the 'needle' string.
# The worst-case scenario is when the 'needle' is not found in the 'haystack', in which case we will have to compare every character of the 'haystack' with the 'needle'.
# The space complexity of this solution is O(1) because we are not using any extra space that grows with the input size.
# We are only using a constant amount of space to store the lengths of the 'haystack' and 'needle' strings.
# Therefore, this solution is efficient in terms of space complexity.

# An alternative approach to solving this problem is to use the built-in string method 'find' in Python.
# The 'find' method returns the index of the first occurrence of the substring in the string, or -1 if the substring is not found.
# We can use this method to find the starting position of the 'needle' in the 'haystack'.
# Here is an example of how we can use the 'find' method to solve the problem:

def findSubstringStart(haystack, needle):
    return haystack.find(needle) 