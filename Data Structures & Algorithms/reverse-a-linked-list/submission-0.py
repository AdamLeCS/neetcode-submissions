# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        new_head = None
        curr_node = head
        next_node = head.next
        while (next_node != None):
            curr_node.next = new_head
            new_head = curr_node
            curr_node = next_node
            next_node = next_node.next
        curr_node.next = new_head
        return curr_node

            
        