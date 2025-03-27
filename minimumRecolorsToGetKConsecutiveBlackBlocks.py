# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.
# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.
 

# Constraints:

# n == blocks.length
# 1 <= n <= 100
# blocks[i] is either 'W' or 'B'.
# 1 <= k <= n

# My Solution:
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        l,r=0,(k-1)
        count=float('+inf')
        while r<len(blocks):
            steps=0
            for i in range(l,r+1):
                if blocks[i]=='W':
                    steps+=1
            count=min(count,steps)
            l+=1
            r=l+(k-1)


        return count
    
# Time complexity: O(n)
# Space complexity: O(1)


# Other Solutions:
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        l,r=0,(k-1)
        count=float('+inf')
        while r<len(blocks):
            steps=blocks[l:r+1].count('W')
            count=min(count,steps)
            l+=1
            r=l+(k-1)


        return count
    
# Time complexity: O(n)
# Space complexity: O(1)


# Other Solutions:
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        n = len(blocks)
        white_count = blocks[:k].count('W')
        min_re = white_count

        for i in range(k, n):
            if blocks[i - k] == 'W':
                white_count -= 1
            if blocks[i] == 'W':
                white_count += 1
            min_re = min(min_re, white_count)
        return min_re
        

# Time complexity: O(n)
# Space complexity: O(1)