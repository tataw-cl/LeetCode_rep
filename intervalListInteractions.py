# 986. Interval List Intersections
# Solved
# Medium
# Topics
# Companies
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

# Example 1:


# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Example 2:

# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
 

# Constraints:

# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109 
# endj < startj+1


#My Solution:
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            if end1 < start2:
                i += 1
            elif end2 < start1:
                j += 1
            else:
                res.append([max(start1, start2), min(end1, end2)])
                if end1 < end2:
                    i += 1
                else:
                    j += 1
        return res
    

    #Time Complexity: O(n + m), where n and m are the lengths of firstList and secondList, respectively.
    #Space Complexity: O(1), since we are using a constant amount of space for the pointers and the result list.

