# 2023. Number of Pairs of Strings With Concatenation Equal to Target
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

 

# Example 1:

# Input: nums = ["777","7","77","77"], target = "7777"
# Output: 4
# Explanation: Valid pairs are:
# - (0, 1): "777" + "7"
# - (1, 0): "7" + "777"
# - (2, 3): "77" + "77"
# - (3, 2): "77" + "77"
# Example 2:

# Input: nums = ["123","4","12","34"], target = "1234"
# Output: 2
# Explanation: Valid pairs are:
# - (0, 1): "123" + "4"
# - (2, 3): "12" + "34"
# Example 3:

# Input: nums = ["1","1","1"], target = "11"
# Output: 6
# Explanation: Valid pairs are:
# - (0, 1): "1" + "1"
# - (1, 0): "1" + "1"
# - (0, 2): "1" + "1"
# - (2, 0): "1" + "1"
# - (1, 2): "1" + "1"
# - (2, 1): "1" + "1"
 

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i].length <= 100
# 2 <= target.length <= 100
# nums[i] and target consist of digits.
# nums[i] and target do not have leading zeros.

# My solution:
class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        valid_pairs=0
        for i in range(len(nums)):
            j=len(nums)-1
            while j>=0:
                if j!=i and nums[i]+nums[j]==target:
                    valid_pairs +=1
                j-=1
        return valid_pairs
    
# Time complexity: O(n^2)
# Space complexity: O(1)

#Comparing with other solutions:
class Solution(object):
    def numOfPairs(self, nums, target):
        import collections as c
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        c = Counter(nums)
        return sum([c[target[len(item):]] - int(item == target[len(item):]) for item in nums if target[:len(item)] == item and target[len(item):] in c])
    
# Time complexity: O(n)
# Space complexity: O(n)