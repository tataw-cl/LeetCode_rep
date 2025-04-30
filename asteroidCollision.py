# 735. Asteroid Collision
# Solved
# Medium
# Topics
# Companies
# Hint
# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0


#My Solution:
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if  stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] > abs(asteroid) :
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack
                    

        #Time Complexity: O(n)
        #Space Complexity: O(n)
# 1. The time complexity is O(n) because we are iterating through the list of asteroids once.
# 2. The space complexity is O(n) because we are using a stack to store the asteroids that are not destroyed. In the worst case, all asteroids could be stored in the stack.


#Other Solutions:
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # Collision: Compare top of stack with current asteroid
                if stack[-1] < -asteroid:
                    stack.pop()  # top explodes, keep checking
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()  # both explode
                break  # current asteroid is destroyed, don't push
            else:
                stack.append(asteroid)  # no collision, push it
        
        return stack
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
