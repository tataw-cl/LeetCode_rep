# 2418. Sort the People
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

 

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 

# Constraints:

# n == names.length == heights.length
# 1 <= n <= 103
# 1 <= names[i].length <= 20
# 1 <= heights[i] <= 105
# names[i] consists of lower and upper case English letters.
# All the values of heights are distinct.

#My Solution:
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        res=[]
        namesTuple=list(zip(heights, names))
        for i in range(len(namesTuple)):
            swapped=False
            for j in range(0, (len(namesTuple)-i)-1):
                if namesTuple[j]<namesTuple[j+1]:
                    namesTuple[j],namesTuple[j+1]=namesTuple[j+1],namesTuple[j]
                    swapped=True
            if not swapped:
                break
        for height,name in namesTuple:
            res.append(name)

        return res
    
    #This is a brute force solution with O(n^2) time complexity and O(1) space complexity.
    # Time complexity: O(n^2)
    # Space complexity: O(1)

    #Optimal Solution:
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
    #This is an optimal solution with O(nlogn) time complexity and O(n) space complexity.