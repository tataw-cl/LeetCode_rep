# 475. Heaters
# Solved
# Medium
# Topics
# Companies
# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

# Every house can be warmed, as long as the house is within the heater's warm radius range. 

# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

# Notice that all the heaters follow your radius standard, and the warm radius will the same.

 

# Example 1:

# Input: houses = [1,2,3], heaters = [2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
# Example 2:

# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.
# Example 3:

# Input: houses = [1,5], heaters = [2]
# Output: 3
 

# Constraints:

# 1 <= houses.length, heaters.length <= 3 * 104
# 1 <= houses[i], heaters[i] <= 109


#My Solution:
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        
        def findClosestHeater(house):
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        max_radius = 0
        
        for house in houses:
            index = findClosestHeater(house)
            radius = float('inf')
            
            if index < len(heaters):
                radius = min(radius, abs(heaters[index] - house))
            if index > 0:
                radius = min(radius, abs(heaters[index - 1] - house))
            
            max_radius = max(max_radius, radius)
        
        return max_radius
    
# Time Complexity: O(n log m), where n is the number of houses and m is the number of heaters.
# Space Complexity: O(1), as we are using a constant amount of space for variables.

