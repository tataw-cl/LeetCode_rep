# 2305. Fair Distribution of Cookies
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

# Return the minimum unfairness of all distributions.

 

# Example 1:

# Input: cookies = [8,15,10,20,8], k = 2
# Output: 31
# Explanation: One optimal distribution is [8,15,8] and [10,20]
# - The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
# - The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
# The unfairness of the distribution is max(31,30) = 31.
# It can be shown that there is no distribution with an unfairness less than 31.
# Example 2:

# Input: cookies = [6,1,3,2,2,4,1,2], k = 3
# Output: 7
# Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
# - The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
# - The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
# - The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
# The unfairness of the distribution is max(7,7,7) = 7.
# It can be shown that there is no distribution with an unfairness less than 7.
 

# Constraints:

# 2 <= cookies.length <= 8
# 1 <= cookies[i] <= 105
# 2 <= k <= cookies.length


#My Solution:
class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        self.res=float("+inf")
        dist=[0] * k

        def backtrack(i,dist):
            if i == len(cookies):
                self.res=min(self.res, max(dist))
                return
            
            if max(dist) >= self.res:
                return

            for j in range(k):
                dist[j]+=cookies[i]
                backtrack(i+1, dist)
                dist[j] -= cookies[i]

                if dist[j]==0:
                    break
  
        
        backtrack(0,dist)
        return self.res
    
# Time Complexity: O(k^n) where n is the number of cookies and k is the number of children.
# Space Complexity: O(n + k) where n is the number of cookies and k is the number of children.
# The recursion stack can go up to n levels deep, and we maintain a distribution array of size k.


#Other Solution:
class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cookies)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        
        for mask in range(1 << n):
            for i in range(n):
                if not (mask & (1 << i)):  # If cookie i is not included in the mask
                    new_mask = mask | (1 << i)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + cookies[i])
        
        return min(dp[mask] for mask in range(1 << n) if bin(mask).count('1') == k)
    
    #Time Complexity: O(2^n * n)
    #Space Complexity: O(2^n)

