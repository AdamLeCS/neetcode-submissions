# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        head = tail
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                head.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val, None)
                list2 = list2.next
            head = head.next
        
        if (list1 == None):
            while(list2 != None):
                head.next = ListNode(list2.val, None)
                list2 = list2.next
                head = head.next
        else:
            while(list1 != None):
                head.next = ListNode(list1.val, None)
                list1 = list1.next
                head = head.next
        return tail.next
        