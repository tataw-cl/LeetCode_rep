# 969. Pancake Sorting
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers arr, sort the array by performing a series of pancake flips.

# In one pancake flip we do the following steps:

# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

 

# Example 1:

# Input: arr = [3,2,4,1]
# Output: [4,2,4,3]
# Explanation: 
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: arr = [3, 2, 4, 1]
# After 1st flip (k = 4): arr = [1, 4, 2, 3]
# After 2nd flip (k = 2): arr = [4, 1, 2, 3]
# After 3rd flip (k = 4): arr = [3, 2, 1, 4]
# After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
# Example 2:

# Input: arr = [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip anything.
# Note that other answers, such as [3, 3], would also be accepted.
 

# Constraints:

# 1 <= arr.length <= 100
# 1 <= arr[i] <= arr.length
# All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).


#My Solution:
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res=[]
        def flip(point):
            for i in range(point//2+1):
                temp=arr[i]
                arr[i]=arr[point-i]
                arr[point-i]=temp

        n=len(arr)
        
        for j in range(n-1, 0, -1):
            for k in range(1,j+1):
                if arr[k]==j+1:
                    flip(k)
                    res.append(k+1)
                    break
            flip(j)
            res.append(j+1)



        return res
    
# Time Complexity: O(n^2) - The outer loop runs n-1 times, and the inner loop can run up to n times in the worst case.
# Space Complexity: O(1) - The space used is constant, as we are only using a few variables and the output list.


#Other Solution:
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(arr)
        
        for i in range(n, 1, -1):
            max_index = arr.index(i)
            if max_index != i - 1:
                if max_index != 0:
                    res.append(max_index + 1)  # Flip to bring max to front
                    arr[:max_index + 1] = arr[:max_index + 1][::-1]
                res.append(i)  # Flip to move max to its final position
                arr[:i] = arr[:i][::-1]
        
        return res
    
# Time Complexity: O(n^2) - The outer loop runs n times, and the index search can take up to n time in the worst case.
# Space Complexity: O(1) - The space used is constant, as we are only using a few variables and the output list.
