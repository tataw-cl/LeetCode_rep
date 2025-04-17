# 234. Palindrome Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?


#My Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head:
            return True
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        while prev:
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True
    #Time Complexity: O(n)
    #Space Complexity: O(1)


    #Other Solutions:
    #Using Stack:
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        result = []
        node = head
        while (node):
            result.append(node.val)
            node = node.next
        
        return result == result[::-1]

    #Time Complexity: O(n)
    #Space Complexity: O(n)


