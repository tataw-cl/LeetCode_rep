# 347. Top K Frequent Elements
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


#My Solution:
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        from collections import Counter
        numCount = Counter(nums)
        
        buckets = [[] for _ in range(n+1) ]

        for num, freq in numCount.items():
            buckets[freq].append(num)

        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
                    break

    #Time Complexity: O(n)
    #Space Complexity: O(n)


#Other Solution:
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        return [num for num, _ in count.most_common(k)]
    
    #Time Complexity: O(n log k), where n is the number of elements in nums.
    #Space Complexity: O(n), for storing the frequency count.

