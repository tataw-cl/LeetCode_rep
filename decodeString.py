
# Code
# Testcase
# Testcase
# Test Result
# 394. Decode String
# Solved
# Medium
# Topics
# Companies
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].


#My Solution:
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums=[]
        words=[]
        word=''
        num=0
        for i in range(len(s)):
            if (s[i]).isdigit():
                num=num*10 + int(s[i])
            elif s[i] == '[':
                nums.append(num)
                words.append(word)
                num=0
                word=''
            elif s[i]==']':
                repeats=nums.pop()
                lastWord=words.pop()
                word=lastWord + word*repeats
            else:
                word+=s[i]

        return word


        #Time Complexity: O(n)
        #Space Complexity: O(n)

    

#Other Solutions:
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_str = ''
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ''
                current_num = 0
            elif char == ']':
                last_str, num = stack.pop()
                current_str = last_str + current_str * num
            else:
                current_str += char
        
        return current_str

        #Time Complexity: O(n)
        #Space Complexity: O(n)


        #Other Solution:
        class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        temp=0
        for i in s:
            if i.isdigit():
                temp=temp*10+int(i)
            elif i=='[':
                stack.append(temp)
                temp=0
                stack.append(i)
            elif i==']':
                temp_str=''
                while stack[-1]!='[':
                    temp_str+=stack.pop()
                stack.pop()
                num=stack.pop()
                temp_res=temp_str[::-1]*num
                for j in temp_res:
                    stack.append(j)
            else:
                stack.append(i)
        return ''.join(stack)


        #Time Complexity: O(n)
        #Space Complexity: O(n)

