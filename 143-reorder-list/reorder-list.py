# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        # queue and get everything and popleft(), pop() nad connect the nodes that way 
        
        """
        # reverse the second half of the linked list 
        # and set a pointer to the second half and iterate through it 
        
        if not head.next:
            return head
        
        dummy = ListNode()  
        res = dummy
        secondHalfPointer = head
        
        slow, fast = head, head 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        if fast:
            # to account for the odd number lists, since we are iteraitng first half
            # of the list first, we want to not include this in the thing 
            slow = slow.next  
        
        while secondHalfPointer.next != slow:
            secondHalfPointer = secondHalfPointer.next
        
        startofSecondHalf = self.reverse(slow)
        
        secondHalfPointer.next = startofSecondHalf
        secondHalfPointer = secondHalfPointer.next
        
        curr = head 
        while curr != startofSecondHalf:
            dummy.next = curr
            curr = curr.next 
            dummy = dummy.next 
            if secondHalfPointer:
                # accounts for odd where there is more for the first half 
                dummy.next = secondHalfPointer
                secondHalfPointer = secondHalfPointer.next
                dummy = dummy.next
        dummy.next = None
        return res.next
        
    def reverse(self, slow):
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        return prev
        
        
        
        
        