# 24. Swap Nodes in Pairs
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:



# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


#My Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        dummy=ListNode(-1,head)
        curr=head
        prev=dummy
        while curr and curr.next:
            #Save some points
            nextSpot=curr.next.next
            temp=curr.next

            #actual reversal
            temp.next=curr
            curr.next=nextSpot
            prev.next=temp
            
            #points for the next iteration
            prev=curr
            curr=nextSpot

        return dummy.next

        #Time Complexity: O(n)
        # Space Complexity: O(1)


        ##Other Solutions:
    class Solution(object):
        def swapPairs(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            if not head or not head.next:
                return head
            
            # Swap the first two nodes
            new_head = head.next
            head.next = self.swapPairs(new_head.next)
            new_head.next = head
            
            return new_head

            #Time Complexity: O(n)
            # Space Complexity: O(1)

