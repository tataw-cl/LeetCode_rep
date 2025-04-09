# 2062. Count Vowel Substrings of a String
# Solved
# Easy
# Topics
# Companies
# Hint
# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

# Given a string word, return the number of vowel substrings in word.

 

# Example 1:

# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
# Example 2:

# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.
# Example 3:

# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase English letters only.


#My Solution:
class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        count = 0

       
        for i in range(n):
            unique_vowels = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break  
                unique_vowels.add(word[j])
                if len(unique_vowels) == 5:
                    count += 1

        return count
    

    #Time complexity: O(n^2) where n is the length of the input string.
    #Space complexity: O(1) because we are using a constant amount of space.


#Other Solutions:
class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        count = 0
        
        for i in range(n):
            if word[i] in vowels:
                j = i
                while j < n and word[j] in vowels:
                    j += 1
                count += (j - i) * (j - i + 1) // 2
                i = j - 1
        
        return count
    
    #Time complexity: O(n^2) where n is the length of the input string.
    #Space complexity: O(1) because we are using a constant amount of space.


    #Other Solutions:
    class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set("aeiou")
        count = 0
        start = left = 0  # `start` marks the last valid start position
        freq = {}  # To track vowel frequencies

        for right, char in enumerate(word):
            if char in vowels:
                freq[char] = freq.get(char, 0) + 1

                while len(freq) == 5:  # All vowels present
                    freq[word[left]] -= 1
                    if freq[word[left]] == 0:
                        del freq[word[left]]
                    left += 1  # Shrink window from left
                
                count += (left - start)  # Count substrings from `start` to `left-1`
            else:
                freq.clear()
                start = left = right + 1  # Reset at consonants

        return count
    

    #Time complexity: O(n) where n is the length of the input string.
    #Space complexity: O(1) because we are using a constant amount of space.