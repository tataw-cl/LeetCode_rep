# 2367. Number of Arithmetic Triplets
# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

 

# Example 1:

# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
# Example 2:

# Input: nums = [4,5,6,7,8,9], diff = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
 

# Constraints:

# 3 <= nums.length <= 200
# 0 <= nums[i] <= 200
# 1 <= diff <= 50
# nums is strictly increasing.

# My solution:
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        total=0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i]+diff==nums[j]:
                    for k in range(j,len(nums)):
                        if nums[j]+diff==nums[k]:
                            total+=1
        return total
# Time complexity: O(n^3)
# Space complexity: O(1)
#Comparing with other solutions:
class Solution(object):
    def countTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count = {}
        ans = 0
        
        # Count the occurrences of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Calculate the number of arithmetic triplets
        for num in nums:
            if num + diff in count and num + 2 * diff in count:
                ans += count[num + diff] * count[num + 2 * diff]
        
        return ans
# Time complexity: O(n)
# Space complexity: O(n)

#Comparing with other solutions:
# more efficient solution than the previous ones
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        from collections import Counter
        total=0
        count=Counter(nums)
        for i in nums:
            if i+diff in count and i+(diff*2) in count:
                total +=1
        return total  
# Time complexity: O(n)
# Space complexity: O(n)