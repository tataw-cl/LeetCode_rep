# 1029. Two City Scheduling
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

# Example 1:

# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
# Example 2:

# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859
# Example 3:

# Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# Output: 3086
 

# Constraints:

# 2 * n == costs.length
# 2 <= costs.length <= 100
# costs.length is even.
# 1 <= aCosti, bCosti <= 1000


#My Solution:
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        res=0
        n=len(costs)
        def heuristicFunc(diff):
            a,b = diff
            return a-b

        costs.sort(key = heuristicFunc)

        for i in range(n):
            if i < n//2:
                res += costs[i][0]
            else:
                res += costs[i][1]
        
        return res
    
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) since we are using a constant amount of extra space


#Other Solution:
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Sort the costs based on the difference between the cost of city A and city B
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total_cost = 0
        
        # Sum the costs for the first n people to go to city A and the last n people to go to city B
        for i in range(n):
            total_cost += costs[i][0]  # City A cost for first n people
            total_cost += costs[i + n][1]  # City B cost for last n people
            
        return total_cost
    
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) since we are using a constant amount of extra space

