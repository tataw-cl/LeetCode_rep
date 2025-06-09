# 47. Permutations II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10


# My Solution:
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        usedVal=[False]*len(nums)
        def backtrack(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return

            for j in range(len(nums)):
                if usedVal[j]:
                    continue

                if j > 0 and nums[j]==nums[j-1] and not usedVal[j-1]:
                    continue


                usedVal[j]=True
                arr.append(nums[j])
                backtrack(arr)
                arr.pop()
                usedVal[j]=False

            
        backtrack([])

        return res
    
    # Time Complexity: O(n * n!), where n is the length of nums.
# The n! accounts for the number of permutations, and the n accounts for the time taken to copy the current permutation into the result list.
# Space Complexity: O(n), where n is the length of nums.
# The space is used for the recursion stack and the result list.

        
#Other Solution:        
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        nums.sort()  # Sort to handle duplicates
        backtrack(0)
        return result
    
    #Time Complexity: O(n * n!), where n is the length of nums.
    # The n! accounts for the number of permutations, and the n accounts for the time taken to copy the current permutation into the result list.
# Space Complexity: O(n), where n is the length of nums.
# The space is used for the recursion stack and the result list.
