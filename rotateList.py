
# Code
# Code
# Code Sample
# Testcase
# Testcase
# Test Result
# 61. Rotate List
# Solved
# Medium
# Topics
# Companies
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


#My Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        
        count=0
        current=head
        #Iterate through to get the number of elements in the list
        while current:
            count+=1
            current=current.next

        #check to make sure that k in less than length of list
        k=k%count
        if k==0:
            return head

        #K times, move the last element to point to first and the second last to point to None
        #Move to the last index
        last=head
        while last.next:
            last=last.next
        
        #Point last index to the head of LinkedList
        last.next=head

        #iterate to the cutoff point and point it to none
        cutoffPoint=count-k
        steps=1
        newEnd=head
        while steps < cutoffPoint:
            newEnd=newEnd.next
            steps+=1
        newHead=newEnd.next
        newEnd.next=None
        
        return newHead
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)


#
#Other Solutions:
#Using a dummy node:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        
        dummy=ListNode(-1)
        dummy.next=head
        
        count=0
        current=head
        #Iterate through to get the number of elements in the list
        while current:
            count+=1
            current=current.next

        #check to make sure that k in less than length of list
        k=k%count
        if k==0:
            return head

        #K times, move the last element to point to first and the second last to point to None
        #Move to the last index
        last=dummy
        while last.next:
            last=last.next
        #Point last index to the head of LinkedList
        last.next=head
        #iterate to the cutoff point and point it to none
        cutoffPoint=count-k
        steps=1
        newEnd=dummy
        while steps < cutoffPoint:
            newEnd=newEnd.next
            steps+=1
        newHead=newEnd.next
        newEnd.next=None
        return newHead
    

    #Time Complexity: O(n)
    #Space Complexity: O(1)