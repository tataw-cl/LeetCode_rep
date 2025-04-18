# 1679. Max Number of K-Sum Pairs
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109


#My Solution:
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        l,r=0,len(nums)-1
        nums.sort()
        while l<r:
            if nums[l]+nums[r]>k:
                r-=1
            elif nums[l]+nums[r]<k:
                l+=1
            else:
                res+=1
                l+=1
                r-=1

        return res

        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)
        #The sorting takes O(nlogn) time and the two pointers take O(n) time.
        #So the overall time complexity is O(nlogn+n)=O(nlogn).


#Other Solutions:
#Using Counter:
from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=Counter(nums)
        res=0
        for num in count:
            if k-num in count:
                if num==k-num:
                    res+=count[num]//2
                else:
                    res+=min(count[num],count[k-num])
        return res//2

#Time complexity: O(n)
#Space complexity: O(n)
