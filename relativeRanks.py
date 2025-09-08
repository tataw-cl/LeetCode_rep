# 506. Relative Ranks
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

# Example 1:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

 

# Constraints:

# n == score.length
# 1 <= n <= 104
# 0 <= score[i] <= 106
# All the values in score are unique.


#My solution:
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        res = [""] * n
        numDict = {}

        for i in range(n):
            numDict[score[i]] = i

        score.sort(reverse = True)

        for i in range(n):
            index = numDict[score[i]]
            if i == 0:
                res[index] = "Gold Medal"
            elif i == 1:
                res[index] = "Silver Medal"
            elif i == 2:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(i+1)

        return res
    

    #Time complexity: O(n log n) due to sorting
    #Space complexity: O(n) for the numDict and output list


#Other solution:
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_map = {}
        
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        return [rank_map[s] for s in score]
    
    #Time complexity: O(n log n) due to sorting
    #Space complexity: O(n) for the rank_map and output list


#Other solution:
#Using a heap
import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        max_heap = [-s for s in score]
        heapq.heapify(max_heap)
        
        rank_map = {}
        for i in range(n):
            curr_score = -heapq.heappop(max_heap)
            if i == 0:
                rank_map[curr_score] = "Gold Medal"
            elif i == 1:
                rank_map[curr_score] = "Silver Medal"
            elif i == 2:
                rank_map[curr_score] = "Bronze Medal"
            else:
                rank_map[curr_score] = str(i + 1)
        
        return [rank_map[s] for s in score]
    
    #Time complexity: O(n log n) due to heap operations
    #Space complexity: O(n) for the rank_map and output list
