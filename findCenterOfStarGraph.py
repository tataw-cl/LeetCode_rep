# 1791. Find Center of Star Graph
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

# Example 1:


# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
# Example 2:

# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
 

# Constraints:

# 3 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.

#My Solution:
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        d=defaultdict(int)
        for edge1,edge2 in edges:
            d[edge1]+=1
            d[edge2]+=1
        for node in d:
            if d[node]==len(edges):
                return node
            
# Time Complexity: O(n) - We iterate through the edges once to build the frequency dictionary.
# Space Complexity: O(n) - We use a dictionary to store the frequency of each node, which can grow with the number of nodes in the graph.
   

   #Other Solution:
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # The center of the star graph will be the node that appears in both edges
        return (set(edges[0]) & set(edges[1])).pop()
    
    #Time Complexity: O(1) - We only check the first two edges.
    #Space Complexity: O(1) - We are not using any additional data structures that grow with input size.
