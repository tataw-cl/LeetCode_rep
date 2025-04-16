# 876. Middle of the Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


#My Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummy=ListNode(-1)
        # dummy=head
        if not head:
            return
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
    

#Time Complexity: O(n)
#Space Complexity: O(1)



#Other Solutions:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummy=ListNode(-1)
        # dummy=head
        current=head
        count=0
        while current:
            current=current.next
            count+=1
        middleVal=(count//2)+1
        middle=head
        steps=1
        while steps<middleVal:
            middle=middle.next
            steps+=1
        return middle
    

#Time Complexity: O(n)
#Space Complexity: O(1)