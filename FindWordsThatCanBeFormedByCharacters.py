# 1160. Find Words That Can Be Formed by Characters
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.

#My solution:

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char=list(chars)
        result=0
        char_Counter=Counter(char)
        for word in words:
            good=True
            word_Counter=Counter(word)
            for occurence in word_Counter:
                if word_Counter[occurence] > char_Counter[occurence]:
                    good=False
            if good==True:
                result+=len(word)
        return result
    
    #Other solutions:
    class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        for word in words :
            l = 0
            for c in word[::] :
                if word.count(c) <= chars.count(c) :
                    l += 1
                else :
                    break
            if(l == len(word)):
                res += l

        return res