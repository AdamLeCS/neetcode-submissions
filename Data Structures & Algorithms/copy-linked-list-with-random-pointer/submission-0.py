"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # mapping between node -> index
        # second mapping between index -> rand index
        # create second list without random and update node -> index mapping
        # use second mapping for random

        curr = head
        index = 1
        node_indexes = {}
        index_to_rand = {}
        # node to index
        while (curr != None):
            node_indexes[curr] = index
            curr = curr.next
            index += 1
        # index to rand index
        curr = head
        index = 1
        while (curr != None):
            index_to_rand[index] = node_indexes.get(curr.random, 0) # 0 is null ptr
            curr = curr.next
            index += 1
        
        # create new list
        node_indexes.clear()
        index = 1
        curr = head
        new_list = Node(0)
        curr_new = new_list
        while (curr != None):
            new_node = Node(curr.val)
            curr_new.next = new_node
            node_indexes[index] = new_node
            curr = curr.next
            curr_new = curr_new.next
            index += 1
        
        index = 1
        curr_new = new_list.next
        while (curr_new != None):
            curr_new.random = node_indexes.get(index_to_rand.get(index, 0), None)
            curr_new = curr_new.next
            index += 1
        return new_list.next
        