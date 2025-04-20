# 86. Partition List
# Solved
# Medium
# Topics
# Companies
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


#My Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        #Use two linkedLists to store values less than x and ones more than
        dummy1=ListNode(-1)
        dummy1Head=dummy1
        dummy2=ListNode(-1)
        dummy2Head=dummy2
        current=head
        while current:
            if current.val<x:
                dummy1.next=ListNode(current.val)
                dummy1=dummy1.next
            
            else:
                dummy2.next=ListNode(current.val)
                dummy2=dummy2.next

            current=current.next

        dummy1.next=dummy2Head.next

        return dummy1Head.next

    #Time Complexity: O(n)
    #Space Complexity: O(1)
