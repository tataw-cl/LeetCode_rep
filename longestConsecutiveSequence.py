# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


# My Solution:
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        nums.sort()
        r=0
        if len (nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        length=1
        while r<len(nums)-1:
            if nums[r+1]-nums[r]==1:
                length+=1
            elif nums[r+1]==nums[r]:
                length=length
            else:
                length=1
            res=max(res,length)
            r+=1
        return res
    
    #Time complexity: O(nlogn)
    #Space complexity: O(1)



# Other solution:
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet=set(nums)
        res=0
        for num in numsSet:
            if num-1 not in numsSet:
                count=1
                while num+1 in numsSet:
                    count+=1
                    num+=1
                res=max(res,count)
        return res
    
    #Time complexity: O(n)
    #Space complexity: O(n)