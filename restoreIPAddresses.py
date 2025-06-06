# 93. Restore IP Addresses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:

# 1 <= s.length <= 20
# s consists of digits only.


#My Solution:
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        
        if len(s) > 12:
            return res
        
        def backtrack(i,dots,currentIP):
            if i==len(s) and dots==4:
                res.append(currentIP[:-1])
                return

            if dots>4 or i>len(s):
                return
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i==j or s[i]!='0'):
                    backtrack(j+1,dots+1,currentIP + s[i:j+1] + ".")

        backtrack(0,0,"")
        return res
    
    #Time Complexity: O(3^4) = O(81) since we can have at most 3 choices for each of the 4 segments.
# Space Complexity: O(1) for the result storage, as the maximum number of valid IP addresses is limited.


#Other Solution:
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            
            for i in range(1, 4):  # Length of the segment can be 1 to 3
                if start + i <= len(s):
                    segment = s[start:start + i]
                    if (len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)):
                        backtrack(start + i, path + [segment])
        
        backtrack(0, [])
        return res
    
    #Time Complexity: O(3^4) = O(81) since we can have at most 3 choices for each of the 4 segments.
    #Space Complexity: O(1) for the result storage, as the maximum number of valid IP addresses is limited.

