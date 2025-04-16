# 206. Reverse Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


#My Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        prev,current=None,head
        while current:
            temp=current.next #Store value of the current's next pointer
            current.next=prev #now, point the current to the prev node
            prev=current #update the prev node to become the current node for the nexst iteration
            current=temp #now set the current node to the temp(next node) for next iter
        return prev
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)


    #Other Solutions:
    #Using Recursion:
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution(object):
        def reverseList(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            if not head or not head.next:
                return head
            new_head=self.reverseList(head.next)
            head.next.next=head
            head.next=None
            return new_head
        
        #Time Complexity: O(n)
        #Space Complexity: O(n) because of the recursion stack space

