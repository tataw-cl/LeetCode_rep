# 2574. Left and Right Sum Differences
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.

 

# Example 1:

# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
# Example 2:

# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 105

#My solution:
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        left,right=0,sum(nums)
        for i in range(len(nums)):
            left=sum(nums)-right
            right-=nums[i]
            answer.append(abs(left-right))
        return answer

        #Time complexity: O(n)
        #Space complexity: O(n)

#Other solutions:

        class Solution(object):
    def leftRightDifference(self, nums):
        
        ans = []
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            ans.append(abs(left-right))
        return ans
        


#Other solutions:
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = []
        rightSum = []
        ans = []
        n = len(nums)
        
        tmpSum = 0
        for i in range(0, n):
            leftSum.append(tmpSum)
            tmpSum += nums[i]
        
        tmpSum = 0
        for j in range(n-1, -1, -1):
            rightSum.append(tmpSum)
            tmpSum += nums[j]
        rightSum.reverse()
        
        tmpSub = 0
        for k in range(0, n):
            tmpSub = abs(leftSum[k] - rightSum[k])
            ans.append(tmpSub)
        
        return ans


        #Other solutions:
        class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = []
        rightSum = []
        if len(nums) == 1:
            return [0]
        leftSum.append(0)
        left_total = 0
        for i in range(1, len(nums)):
            left_total += nums[i-1]
            leftSum.append(left_total)
        right_total = leftSum[-1] + nums[-1]
        for i in range(0, len(nums)-1):
            right_total -= nums[i]
            rightSum.append(right_total)
        rightSum.append(0)
        list_out = []
        print(rightSum)
        print(leftSum)
        for i in range(len(rightSum)):
            list_out.append(abs(rightSum[i] - leftSum[i]))
        return list_out

        