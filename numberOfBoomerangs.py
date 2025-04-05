# 447. Number of Boomerangs
# Solved
# Medium
# Topics
# Companies
# You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Return the number of boomerangs.

 

# Example 1:

# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
# Example 2:

# Input: points = [[1,1],[2,2],[3,3]]
# Output: 2
# Example 3:

# Input: points = [[1,1]]
# Output: 0
 

# Constraints:

# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.


#My Solution:
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=0
        for i in points:
            distances=defaultdict(int)
            
            for j in points:
                if i==j:
                    continue
                a=i[0]-j[0]
                b=i[1]-j[1]
                gap=(a*a)+ (b*b)
                distances[gap]+=1

            for count in distances.values():
                if count>1:
                    res+=count*(count-1)

        return res
    

    #Time complexity: O(n^2)
    #Space complexity: O(n)




#Other solution:
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = 0
        for a,b in points:
            counter = {}
            for x,y in points:
                key = (x-a)**2 + (y-b)**2
                if key in counter:
                    n += 2*counter[key]
                    counter[key] += 1
                else:
                    counter[key] = 1
        return n
    
    #Time complexity: O(n^2)
    #Space complexity: O(n)