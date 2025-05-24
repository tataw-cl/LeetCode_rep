# 875. Koko Eating Bananas
# Solved
# Medium
# Topics
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109


#My Solution:
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2
            hours_needed = sum((pile + mid - 1) // mid for pile in piles)

            if hours_needed <= h:
                high = mid
            else:
                low = mid + 1

        return low
    

    #Time Complexity: O(n log m), where n is the number of piles and m is the maximum number of bananas in a pile.
    #Space Complexity: O(1), as we are using a constant amount of space for variables.


    #Other Solutions:
    # Some solutions use a binary search approach to find the minimum speed k.
    # They calculate the total hours needed for each speed and adjust the search range accordingly.
    # Others may use a greedy approach to find the minimum speed by iterating through the piles and calculating the required speed based on the total hours.
    # The binary search approach is generally more efficient for this problem, especially with larger inputs.

