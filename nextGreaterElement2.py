# # 503. Next Greater Element II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
 

# Constraints:

# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109


#My Solution:
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[0]*n
        stack=[]
        for i in range(2*n - 1,-1,-1):
            m=i%n
            while stack and nums[m] >= stack[-1]:
                stack.pop()
            if i < n:
                if stack:
                    res[m]=stack[-1]
                else:
                    res[m]= -1
                

            stack.append(nums[m])


        return res
        
# Time Complexity: O(n)
# Space Complexity: O(n)


#Other Solutions:
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)

        return res
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
