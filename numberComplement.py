# 476. Number Complement
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

 

# Example 1:

# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
# Example 2:

# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

# Constraints:

# 1 <= num < 231
 

# Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

#My Solution:
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)[2:]
        res = "".join("1" if bit == "0" else "0" for bit in b)      
        return int(res,2)

#Time Complexity: O(log n) - because we are converting the number to binary representation.
#Space Complexity: O(log n) - for storing the binary representation of the number.


#Other Solutions:
class Solution(object):
    def findComplement(self, num):
        def decimal_to_binary(n):
            if n == 0:
                return "0"
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary

        def binary_to_decimal(binary_str):
            decimal = 0
            binary_str = binary_str[::-1]  # Reverse the string to process from right to left
            for i in range(len(binary_str)):
                decimal += int(binary_str[i]) * (2 ** i)
            return decimal

        binary = decimal_to_binary(num)
        n = len(binary)

        complement = ''
        for i in range(n):
            if binary[i] == '0':
                complement += '1'
            else:
                complement += '0'

        return binary_to_decimal(complement)        
    

#Time Complexity: O(log n) for converting the number to binary and then back to decimal.
#Space Complexity: O(log n) for storing the binary representation of the number.

