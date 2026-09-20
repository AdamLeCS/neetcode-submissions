# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num_nodes = 0
        temp = head
        while(temp != None):
            num_nodes += 1
            temp = temp.next
        # find the node before the removal node
        num_next = num_nodes - n - 1
        if (num_next == -1): # means that you're removing the head node
            return head.next
        curr = head
        for i in range(num_next):
            curr = curr.next
        curr.next = curr.next.next
        return head