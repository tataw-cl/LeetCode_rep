# 965. Univalued Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

# Example 1:


# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:


# Input: root = [2,2,2,5,2]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100

#My Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return True

            if node.val!=root.val:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)

        #Time Complexity: O(n) where n is the number of nodes in the tree
        #Space Complexity: O(h) where h is the height of the tree due to recursion


#Other Solutions:
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def check(node, value):
            if not node:
                return True
            if node.val != value:
                return False
            return check(node.left, value) and check(node.right, value)

        return check(root, root.val) if root else True
    
#Time Complexity: O(n) where n is the number of nodes in the tree
#Space Complexity: O(h) where h is the height of the tree due to recursion

