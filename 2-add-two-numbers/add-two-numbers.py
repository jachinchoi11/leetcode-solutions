# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # the part about this is that there is some form of carry 
        # so if the sum of the values are over 10 then we have to carry add (number // 10) 
        # and you add number % 10
    

        dummy = ListNode()
        prev = dummy
        carry = 0

        while l1 and l2:
            curr_sum = l1.val + l2.val
            print(curr_sum)
            if carry > 0:
                curr_sum += carry
                carry = 0
            
            carry += (curr_sum // 10)

            new_node = ListNode(curr_sum % 10)
            dummy.next = new_node
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr_sum = l1.val

            if carry > 0:
                curr_sum += (carry)
                carry = 0
            
            carry += (curr_sum // 10)

            new_node = ListNode(curr_sum % 10)
            dummy.next = new_node
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            curr_sum = l2.val

            if carry > 0:
                curr_sum += (carry)
                carry = 0
            
            carry += (curr_sum // 10)

            new_node = ListNode(curr_sum % 10)
            dummy.next = new_node
            dummy = dummy.next
            l2 = l2.next
        
        if carry > 0:
            dummy.next = ListNode(carry)
        
        return prev.next


        


        