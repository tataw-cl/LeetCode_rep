# 19. Remove Nth Node From End of List
# Solved
# Medium
# Topics
# Companies
# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?


#My Solution:
#Using two pointers to find the length of the linked list and then remove the nth node from the end.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        dummy=ListNode(-1)
        dummy.next=head
        fast=dummy
        slow=dummy
        for _ in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)


    #Other Solutions:
    #By counting the length of the linked list and then removing the nth node from the end.
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: Optional[ListNode]
            :type n: int
            :rtype: Optional[ListNode]
            """
            if not head:
                return
            dummy=ListNode(-1)
            dummy.next=head
            length=0
            current=head
            while current:
                length+=1
                current=current.next
            current=dummy
            for _ in range(length-n):
                current=current.next
            current.next=current.next.next
            return dummy.next
        
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #This solution uses O(1) space and O(n) time complexity.