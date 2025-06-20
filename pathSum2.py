# 113. Path Sum II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


#My Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(node,total,path):
            if not node:
                return
            path.append(node.val)
            total+=node.val
            if not node.left and not node.right and total==targetSum:
                    res.append(path[:])
            
            if node.right:
                dfs(node.right,total,path)
            if node.left:
                dfs(node.left,total,path)
                
            path.pop()

        dfs(root,0,[])
        return res
    
    #Time Complexity: O(n) - where n is the number of nodes in the tree, as we visit each node once.
    #Space Complexity: O(h) - where h is the height of the tree, for the recursion stack and the path list.


#Other Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            current_sum += node.val
            path.append(node.val)
            
            if not node.left and not node.right and current_sum == targetSum:
                res.append(path[:])
            
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            
            path.pop()
        
        dfs(root, 0, [])
        return res
    
# Time Complexity: O(n) - where n is the number of nodes in the tree, as we visit each node once.
# Space Complexity: O(h) - where h is the height of the tree, for the recursion stack and the path list.

