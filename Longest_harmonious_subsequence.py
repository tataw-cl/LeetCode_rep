# 594. Longest Harmonious Subsequence
# Easy
# Topics
# Companies
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 2
# Example 3:

# Input: nums = [1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

# My solution:
def findLHS(nums: List[int]) -> int:
    from collections import Counter
    count = Counter(nums)
    res = 0
    for k in count:
        if k+1 in count:
            res = max(res, count[k] + count[k+1])
    return res

# Time complexity: O(n)
# Space complexity: O(n)

#Other solutions:
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0

        d = {}
        met = []

        for num in nums:
            if num not in met:
                d[num] = 1
                met.append(num)
            else:
                d[num] += 1

        for num in nums:
            flag = False
            count1 = 0
            count2 = 0
            count1 += d[num]
            count2 += d[num]
            if num-1 in d:
                flag = True
                count1 += d[num-1]
            elif num+1 in d:
                flag = True
                count2 += d[num+1]
            if flag == False:
                count1 = 0
                count2 = 0
            # print("num:", num, "ans:", ans, "count1", count1, "count2", count2)
            ans = max(ans, max(count1, count2))
            # print("ans:", ans)

        return ans