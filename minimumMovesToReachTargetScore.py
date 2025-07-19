# 2139. Minimum Moves to Reach Target Score
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

# In one move, you can either:

# Increment the current integer by one (i.e., x = x + 1).
# Double the current integer (i.e., x = 2 * x).
# You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

# Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.

 

# Example 1:

# Input: target = 5, maxDoubles = 0
# Output: 4
# Explanation: Keep incrementing by 1 until you reach target.
# Example 2:

# Input: target = 19, maxDoubles = 2
# Output: 7
# Explanation: Initially, x = 1
# Increment 3 times so x = 4
# Double once so x = 8
# Increment once so x = 9
# Double again so x = 18
# Increment once so x = 19
# Example 3:

# Input: target = 10, maxDoubles = 4
# Output: 4
# Explanation: Initially, x = 1
# Increment once so x = 2
# Double once so x = 4
# Increment once so x = 5
# Double again so x = 10
 

# Constraints:

# 1 <= target <= 109
# 0 <= maxDoubles <= 100


#My Solution:
class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        ones = 0
        doubles = maxDoubles
        while doubles > 0 and target > 1:
            if target % 2 == 1:
                ones += 1
            target = target // 2

            doubles -= 1

        ones += target - 1

        moves = ones + (maxDoubles - doubles)

        return moves
    
        #Time Complexity: O(log(target)) for the while loop
        #Space Complexity: O(1) since we are using a constant amount of space
    

#Other Solution:
class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        moves = 0
        
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            moves += 1
        
        moves += (target - 1)  # Remaining increments to reach target from 1
        
        return moves
    
        #Time Complexity: O(log(target)) for the while loop
        #Space Complexity: O(1) since we are using a constant amount of space

