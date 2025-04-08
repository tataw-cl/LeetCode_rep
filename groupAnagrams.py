# 49. Group Anagrams
# Solved
# Medium
# Topics
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


#My Solution:
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramsMap=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            anagramsMap[key].append(word)
        res=list(anagramsMap.values())
        return res

    #Time complexity: O(n*klogk) where n is the number of strings and k is the maximum length of a string.
    #Space complexity: O(n*k) where n is the number of strings and k is the maximum length of a string.
    #The space complexity is O(n*k) because we are storing all the strings in the anagramsMap dictionary.



    #Other Solutions:
    #Using Counter from collections module
    #The Counter class from the collections module can be used to count the frequency of each character in a string.
    #We can use this to create a unique key for each anagram group.
    #This solution has a time complexity of O(n*k) and a space complexity of O(n*k).
    #This is because we are storing all the strings in the anagramsMap dictionary.


    #Implementation:
from collections import Counter
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramsMap=defaultdict(list)
        for word in strs:
            key=tuple(sorted(Counter(word).items()))
            anagramsMap[key].append(word)
        res=list(anagramsMap.values())
        return res

    #Time complexity: O(n*k) where n is the number of strings and k is the maximum length of a string.
    #Space complexity: O(n*k) where n is the number of strings and k is the maximum length of a string.
    #The space complexity is O(n*k) because we are storing all the strings in the anagramsMap dictionary.


    #Other Solution:
    def groupAnagrams(strs):
    from collections import defaultdict

    anagram_map = defaultdict(list)

    for word in strs:
        # 26-length tuple representing character count
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        anagram_map[key].append(word)

    return list(anagram_map.values())

#Time complexity: O(n*k) where n is the number of strings and k is the maximum length of a string.
#Space complexity: O(n*k) where n is the number of strings and k is the maximum length of a string.
#The space complexity is O(n*k) because we are storing all the strings in the anagramsMap dictionary.