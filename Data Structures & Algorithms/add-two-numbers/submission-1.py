# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force solution O(n+m) time O(n+m) space
        new_list = ListNode() # dummy head node
        carry = 0
        curr1 = l1
        curr2 = l2
        curr3 = new_list
        while (curr1 != None and curr2 != None):
            sum = curr1.val + curr2.val + carry
            carry = 1 if sum >= 10 else 0
            curr3.next = ListNode(sum % 10)
            curr1 = curr1.next
            curr2 = curr2.next
            curr3 = curr3.next
        if (curr1 == None and curr2 == None): # if lists are same length
            if carry == 1:
                curr3.next = ListNode(1)
            return new_list.next
        elif (curr1 == None): # will make the curr1 pointer point to whichever list is longer
            curr1 = curr2
        while(curr1 != None):
            sum = curr1.val + carry
            carry = 1 if sum >= 10 else 0
            curr3.next = ListNode(sum % 10)
            curr1 = curr1.next
            curr3 = curr3.next
        if (carry == 1):
            curr3.next = ListNode(1)
        return new_list.next