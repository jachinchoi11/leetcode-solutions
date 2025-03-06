# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # initially my thought process is to maybe go through the list and get its length 
        # and then just travel the length - n 

        # it seems reasonable, but it is a two pass solution 

        # i feel like a one pass solution would be possible here, so maybe using two poitners we can set that offset initially

        # so let the regular pointer go n steps 
            # and then just move them simultaeniosuly until the forward one goes otu of bounds 

        # then we would remove the node using a prev pointer --> so maybe have three pointer 

        prev, ahead = ListNode(), head
        prev.next = head
        dummy = prev

        for _ in range(n):
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            prev = prev.next
        temp = prev.next
        prev.next = prev.next.next
        temp.next = None

        return dummy.next
        
        # 1
        # 1, None

        
