# 974. Subarray Sums Divisible by K
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# 2 <= k <= 104

# My Solution:
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum=0
        modDict=defaultdict(int)
        modDict[0]=1
        res=0
        for num in nums:
            preSum+=num
            remainder=preSum%k
            if remainder in modDict:
                res+=modDict[remainder]
            modDict[remainder]+=1

        return res
    
    ## Time complexity: O(n)
    ## Space complexity: O(n)


    ## Other Solutions:
    class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        prefix_sum =0
        count =0
        mod_count =[0] * k  
        mod_count[0] =1  
        for num in nums:
            prefix_sum +=num
            rem =prefix_sum % k
            if rem < 0:
                rem +=k
            count +=mod_count[rem]
            mod_count[rem] +=1
        return(count)
        
        ## Time complexity: O(n)
        ## Space complexity: O(n)