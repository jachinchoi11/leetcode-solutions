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
        
        # i think we can iterate through the liked list and create the firs thting
        # iterate rhough it again and initialize the random pointers

        curr = head 
        newHead = ListNode(0)
        newCurr = newHead
        dummy = newHead

        # we need to create a hashmap with the value associated with the address of the pointer and then find it and point the thing to it
        address = {}

        while curr:
            # were making the new list with just the next pointers and the value pointers
            newCurr.next = Node(curr.val)
            newCurr = newCurr.next
            address[curr] = newCurr
            curr = curr.next 
        newHead = newHead.next

        while head:
            if head.random:
                random_pointer = head.random
                newHead.random = address[random_pointer]
            newHead = newHead.next
            head = head.next
        return dummy.next


            