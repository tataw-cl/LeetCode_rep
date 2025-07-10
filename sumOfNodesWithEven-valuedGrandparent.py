# 1315. Sum of Nodes with Even-Valued Grandparent
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.

 

# Example 1:


# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
# Example 2:


# Input: root = [1]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100

#My Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        res=0
        queue=deque()
        queue.append((root,None,None))

        while queue:
            node,parent,gparent = queue.popleft()
            if node:
                if gparent and gparent.val % 2 == 0:
                    res += node.val

                if node.left:
                    queue.append((node.left,node,parent))
                if node.right:
                    queue.append((node.right,node,parent))

        return res
    

    #Time Complexity: O(n), where n is the number of nodes in the tree.
    #Space Complexity: O(n), for the queue used in BFS.


    #Other Solutions:
    #Using DFS
    class Solution2(object):
        def sumEvenGrandparent(self, root):
            """
            :type root: Optional[TreeNode]
            :rtype: int
            """
            def dfs(node, parent, grandparent):
                if not node:
                    return 0
                total = 0
                if grandparent and grandparent.val % 2 == 0:
                    total += node.val
                total += dfs(node.left, node, parent) + dfs(node.right, node, parent)
                return total
            
            return dfs(root, None, None)
        
        #Time Complexity: O(n), where n is the number of nodes in the tree.
        #Space Complexity: O(h), where h is the height of the tree (for recursion stack).

