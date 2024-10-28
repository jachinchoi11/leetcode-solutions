# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        carry = 0

        while l1 and l2:
            currNum = 0

            currNum = l1.val + l2.val + carry
            if carry > 0:
                carry -= 1
            if currNum >= 10:
                currNum -= 10
                carry += 1

            dummy.next = ListNode(currNum)
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        while l1:
            currSum = l1.val + carry
            if currSum >= 10:
                currSum -= 10
                carry += 1
            if carry > 0:
                carry -= 1
            dummy.next = ListNode(currSum)
            dummy = dummy.next
            l1 = l1.next      
        
        while l2: 
            currSum = carry + l2.val
            if currSum >= 10:
                currSum -= 10
                carry += 1
            if carry > 0:
                carry -= 1
            dummy.next = ListNode(currSum)
            dummy = dummy.next
            l2 = l2.next 
        if carry != 0:
            dummy.next = ListNode(carry)
        
        return prev.next
        
        





            