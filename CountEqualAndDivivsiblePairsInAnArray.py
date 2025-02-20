# 2176. Count Equal and Divisible Pairs in an Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 

# Example 1:

# Input: nums = [3,1,2,2,2,1,3], k = 2
# Output: 4
# Explanation:
# There are 4 pairs that meet all the requirements:
# - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
# - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
# - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
# - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
# Example 2:

# Input: nums = [1,2,3,4], k = 1
# Output: 0
# Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i], k <= 100

#My Solution:
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        count={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=[]
            count[nums[i]].append(i)
        for indices in count.values():
            n=len(indices)
            for i in range(n):
                for j in range(i+1,n):
                    if indices[i]*indices[j]%k==0:
                        result+=1
        return result

        #Time Complexity: O(n^2)
        #Space Complexity: O(n)

#Other Solution:
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count += 1
        return count
    
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)

#Other Solution:
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq = defaultdict(list)
        count = 0

        for index, value in enumerate(nums):
            freq[value].append(index)
            for index2 in freq[value]:
                if (index * index2) % k == 0 and index2 < index:
                    count += 1

        return count
    
        #Time Complexity: O(n^2)
        #Space Complexity: O(n)