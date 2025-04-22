# 445. Add Two Numbers II
# Solved
# Medium
# Topics
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:

# Input: l1 = [0], l2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
 

# Follow up: Could you solve it without reversing the input lists?


#My Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        val1=0
        val2=0
        curr1=l1
        curr2=l2
        prev=None
        while curr1:
            temp=curr1.next
            curr1.next=prev
            prev=curr1
            curr1=temp

        prev2=None
        while curr2:
            temp=curr2.next
            curr2.next=prev2
            prev2=curr2
            curr2=temp

        res=[]
        carry=0
        while prev or prev2 or carry:
            val=(prev.val if prev else 0 ) +( prev2.val if prev2 else 0) + carry

            #set the values of carry, val and prev/prev2
            carry=val//10
            val=val%10
            res.append(val)

            #Set values for next iteration
            prev=prev.next if prev else None
            prev2=prev2.next if prev2 else None

        dummy=ListNode(-1)
        curr=dummy
        for val in reversed(res):
            curr.next=ListNode(val)
            curr=curr.next

        return dummy.next
    

#     #Time Complexity: O(max(m,n)) where m and n are the lengths of the two linked lists.
#     #Space Complexity: O(max(m,n)) for the new linked list.


#Otherr solution:
#SOlution without reversing the input lists:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        len1 = get_length(l1)
        len2 = get_length(l2)

        # Pad the shorter list with zeros
        if len1 < len2:
            for _ in range(len2 - len1):
                new_node = ListNode(0)
                new_node.next = l1
                l1 = new_node
        elif len2 < len1:
            for _ in range(len1 - len2):
                new_node = ListNode(0)
                new_node.next = l2
                l2 = new_node

        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        # Add the two numbers
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
    
    #Time Complexity: O(max(m,n)) where m and n are the lengths of the two linked lists.
#     #Space Complexity: O(max(m,n)) for the new linked list.


#Another Solution:
#Solution without reversing the input lists and using a stack:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Use stacks to store the digits of the numbers
        stack1, stack2 = [], []

        # Step 1: Push values to stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Step 2: Pop from stacks and add digits
        while stack1 or stack2 or carry:
            sum_val = carry
            if stack1:
                sum_val += stack1.pop()
            if stack2:
                sum_val += stack2.pop()

            carry = sum_val // 10
            node = ListNode(sum_val % 10)
            node.next = head
            head = node  # build result from front

        return head




# #Other Solutions:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Reverse the linked lists
        def reverse_list(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        # Add the two numbers
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Reverse the result list before returning it
        return reverse_list(dummy_head.next)
    

    #Time Complexity: O(max(m,n)) where m and n are the lengths of the two linked lists.
    #Space Complexity: O(max(m,n)) for the new linked list.

