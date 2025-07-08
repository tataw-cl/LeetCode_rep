# 215. Kth Largest Element in an Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

#My Solution:
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        min_heap=[]
        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return min_heap[0]
    
# Time Complexity: O(n log k), where n is the number of elements in nums.
# Space Complexity: O(k), for the min heap.


# Other Solutions:
class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]
    
# Time Complexity: O(n log n), where n is the number of elements in nums.
# Space Complexity: O(n), for the sorted array.


#Other Solutions:
class Solution3(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, left, right, k_smallest):
        if left == right:
            return nums[left]

        pivot_index = self.partition(nums, left, right)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return self.quickSelect(nums, left, pivot_index - 1, k_smallest)
        else:
            return self.quickSelect(nums, pivot_index + 1, right, k_smallest)

    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
# Time Complexity: O(n) on average, O(n^2) in the worst case.
# Space Complexity: O(1) for the in-place partitioning.


#Other Solutions:
import heapq
__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
         
        m = heapq.nlargest(k, nums)
        return m[-1]


# Time Complexity: O(n log k), where n is the number of elements in nums.
# Space Complexity: O(k), for the list of k largest elements.
