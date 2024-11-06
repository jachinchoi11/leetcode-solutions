# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        curr = head 
        hashset = set()

        while curr:
            if curr.val in hashset:
                temp = curr.next 
                prev.next = temp
                curr = temp
            else:
                hashset.add(curr.val)
                curr = curr.next
                prev = prev.next
        
        return dummy.next






