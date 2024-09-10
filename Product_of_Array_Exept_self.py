# 238. Product of Array Except Self
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


# My solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        return [left[i]*right[i] for i in range(n)]
    
# Runtime: 232 ms, faster than 98.68% of Python3 online submissions for Product of Array Except Self.
# Time complexity: O(n)
# Space complexity: O(n)

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
# Other solutions:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        for i in range(1,n):
            res[i]=res[i-1]*nums[i-1]
        right=1
        for i in range(n-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# Sure, let's break down and explain the code from lines 52 to 62 of the Product_of_Array_Except_self.py file. Here is the excerpt:

# Explanation:
# This part of the code calculates the product of all elements to the right of each element in the array nums and multiplies it with the corresponding element in the result array. The result array initially contains the product of all elements to the left of each element.

# Step-by-Step Breakdown:
# Initialize right_product:

# right_product is initialized to 1. This variable will keep track of the product of all elements to the right of the current element as we traverse the array from right to left.
# Traverse the array from right to left:

# The for loop iterates over the array nums from the last element to the first element.
# Update result array:

# For each element at index i, the current value of result[i] (which contains the product of all elements to the left of i) is multiplied by right_product (which contains the product of all elements to the right of i).
# This effectively updates result[i] to be the product of all elements in the array except nums[i].
# Update right_product:

# After updating result[i], right_product is updated by multiplying it with nums[i]. This ensures that right_product contains the product of all elements to the right of the next element in the next iteration.
# Example:
# Let's go through an example to illustrate how this works.

# Input:
# Initial State:
# result array after calculating left products:
# (This means result[0] is the product of elements to the left of nums[0], result[1] is the product of elements to the left of nums[1], and so on.)
# Iteration Details:
# Iteration 1 (i = 3):

# right_product = 1
# result[3] *= right_product → result[3] = 6 * 1 = 6
# right_product *= nums[3] → right_product = 1 * 4 = 4
# Iteration 2 (i = 2):

# right_product = 4
# result[2] *= right_product → result[2] = 2 * 4 = 8
# right_product *= nums[2] → right_product = 4 * 3 = 12
# Iteration 3 (i = 1):

# right_product = 12
# result[1] *= right_product → result[1] = 1 * 12 = 12
# right_product *= nums[1] → right_product = 12 * 2 = 24
# Iteration 4 (i = 0):

# right_product = 24
# result[0] *= right_product → result[0] = 1 * 24 = 24
# right_product *= nums[0] → right_product = 24 * 1 = 24
# Final State:
# result array after calculating right products:
# Conclusion:
# The final result array [24, 12, 8, 6] contains the product of all elements in the array nums except the element at each index. This is the desired output of the problem "Product of Array Except Self". The code achieves this in O(n) time complexity and O(1) space complexity.