# 1561. Maximum Number of Coins You Can Get
# Solved
# Medium
# Topics
# Companies
# Hint
# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with the maximum number of coins.
# Your friend Bob will pick the last pile.
# Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins that you can have.

 

# Example 1:

# Input: piles = [2,4,1,2,7,8]
# Output: 9
# Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
# Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
# The maximum number of coins which you can have are: 7 + 2 = 9.
# On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.
# Example 2:

# Input: piles = [2,4,5]
# Output: 4
# Example 3:

# Input: piles = [9,8,7,6,5,1,2,3,4]
# Output: 18
 

# Constraints:

# 3 <= piles.length <= 105
# piles.length % 3 == 0
# 1 <= piles[i] <= 104


#My  Solution:
class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        res=0
        piles.sort()
        n=len(piles)//3
        while n <len(piles):
            res+=piles[n]
            n+=2
        return res


        #Time complexity: O(nlogn)
        #Space complexity: O(1)
        #The space complexity is O(1) because we are not using any extra space.



# #Other Solutions:
    class Solution(object):
        def maxCoins(self, piles):
            """
            :type piles: List[int]
            :rtype: int
            """
            piles.sort()
            n = len(piles)
            return sum(piles[n//3:n//3*2])
        
            #Time complexity: O(nlogn)
            #Space complexity: O(1)



    
# #Other Solutions:

class Solution(object):
    def maxCoins(self, piles):
        def calculate_frequency(piles, max_val):
            freq = [0] * (max_val + 1)
            for i in piles:
                freq[i] += 1
            return freq

        def collect_coins(freq, max_val, chance):
            coins = 0
            turn = 1
            i = max_val
            while chance != 0:
                if freq[i] > 0:
                    if turn == 1:
                        turn = 0
                    else:
                        chance -= 1
                        turn = 1
                        coins += i
                    freq[i] -= 1
                else:
                    i -= 1
            return coins

        max_val = max(piles)
        freq = calculate_frequency(piles, max_val)
        chance = len(piles) // 3
        return collect_coins(freq, max_val, chance)
    

        #Time complexity: O(n)
        #Space complexity: O(n)
        #The space complexity is O(n) because we are using a frequency array to store the counts of each coin value.