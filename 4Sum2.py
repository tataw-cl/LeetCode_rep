"""454. 4Sum II
Solved
Medium
Topics
Companies
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""

#My solution:
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count=0
        lhs=defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                lhs[(num1+num2)]+=1
        for num3 in nums3:
            for num4 in nums4:
                rhs=-(num3+num4)
                count+=lhs[rhs]
        return 
    
    #Time complexity: O(n^2)
    #Space complexity: O(n^2)
    
#Other Solutions:
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D) 
    
    #Time complexity: O(n^2)
    #Space complexity: O(n^2)

    #Other Solution:
    class Solution(object):
        def fourSumCount(self, A, B, C, D):
            count = 0
            sum_map = {}
            for a in A:
                for b in B:
                    sum_map[a + b] = sum_map.get(a + b, 0) + 1
            for c in C:
                for d in D:
                    count += sum_map.get(-(c + d), 0)
            return count
        
        #Time complexity: O(n^2)
        #Space complexity: O(n^2)