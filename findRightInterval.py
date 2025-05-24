# 436. Find Right Interval
# Solved
# Medium
# Topics
# Companies
# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

# Example 1:

# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.
# Example 2:

# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
# Example 3:

# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
 

# Constraints:

# 1 <= intervals.length <= 2 * 104
# intervals[i].length == 2
# -106 <= starti <= endi <= 106
# The start point of each interval is unique.


#My Solution:
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        sortedIntervals=[]
        n=len(intervals)
        for i in range(n):
            sortedIntervals.append([intervals[i],i])
        sortedIntervals.sort()

        res=[0]*n

        def binSearch(x):
            if sortedIntervals[n-1][0][0] < x:
                return -1

            l,r=0,n-1
            while l<=r:
                mid=l+(r-l)//2
                if sortedIntervals[mid][0][0] >=x:
                    r=mid-1
                else:
                    l=mid+1
            return sortedIntervals[l][1]

        for i in range(n):
            res[i]=binSearch(intervals[i][1])
        
        return res
    
    #Time Complexity: O(n log n) for sorting the intervals and O(n log n) for binary search, resulting in O(n log n) overall.
    #Space Complexity: O(n) for storing the sorted intervals and the result list.


    #Other Solutions:
    def findRightInterval2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        sorted_intervals = sorted((start, i) for i, (start, end) in enumerate(intervals))
        result = []
        
        for start, end in intervals:
            idx = bisect.bisect_left(sorted_intervals, (end,))
            result.append(sorted_intervals[idx][1] if idx < len(sorted_intervals) else -1)
        
        return result
    
    #Time Complexity: O(n log n) for sorting the intervals and O(n log n) for binary search, resulting in O(n log n) overall.
    #Space Complexity: O(n) for storing the sorted intervals and the result list.

