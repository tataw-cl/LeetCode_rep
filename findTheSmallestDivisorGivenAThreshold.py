# 1283. Find the Smallest Divisor Given a Threshold
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.

 

# Example 1:

# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
# Example 2:

# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 106
# nums.length <= threshold <= 106



#My Solution:
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def div(divisor):
            total=0
            for num in nums:
                total+=(num+divisor-1)//divisor
            return total


        maxVal=max(nums)
        l,r=1,maxVal
        ans=maxVal
        while l<=r:
            mid=(l+r)//2
            if div(mid)<=threshold:
                ans=mid
                r=mid-1
            else:
                l=mid+1

        return ans


        #Time Complexity: O(nlog m)
        #Space Complexity: O(1)


        #Other Solution:
        
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def ans(nums,mid):
            sumi=0
            for i in nums:
                sumi+=(i + mid - 1) // mid
            print(sumi)
            return sumi
        l=1
        e=max(nums)
        while l<=e:
            mid=(l+e)//2
            if ans(nums,mid)>threshold:
                l=mid+1
                
            else:
                e=mid-1
                
        return l
        

        #Time Complexity: O(nlog m)
        #Space Complexity: O(1)

