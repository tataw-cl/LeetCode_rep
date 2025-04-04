# 2537. Count the Number of Good Subarrays
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.
# Example 2:

# Input: nums = [3,1,4,3,2,2,4], k = 2
# Output: 4
# Explanation: There are 4 different good subarrays:
# - [3,1,4,3,2,2] that has 2 pairs.
# - [3,1,4,3,2,2,4] that has 3 pairs.
# - [1,4,3,2,2,4] that has 2 pairs.
# - [4,3,2,2,4] that has 2 pairs.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 109



# My Solution:
class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l,pairs=0,0
        freqDict=defaultdict(int)
        res=0
        for r in range(len(nums)):
            pairs+=freqDict[nums[r]]
            freqDict[nums[r]]+=1

            while pairs>=k:
                res+=len(nums)-r
                pairs-=(freqDict[nums[l]] -1)
                freqDict[nums[l]]-=1
                l+=1

        return res
    

# Time complexity: O(n)
# Space complexity: O(n)



# Other solution:
class Solution(object):
    def countGood(self, nums, k):
        cmap = defaultdict(int)
        pair = 0
        l = 0
        cnt = 0
        n = len(nums)

        for r, num in enumerate(nums):
            if num not in cmap:
                cmap[num] = 0
            else:
                cmap[num] += 1
                pair += cmap[num] 

            while pair >= k:
                
                pair -= cmap[nums[l]]
                cmap[nums[l]] -= 1
                l += 1

                cnt += n-r

        return cnt
    

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the length of nums.