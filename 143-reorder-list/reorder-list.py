# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # ok somehow you need to get nodes from beginning, end 
        # beginning + 1, end - 1

        # so i think maybe a way we could approach this problem is to reverse the second half
        # we can have a dummy pointer and just merge one by one

        # to find the middle, we use the trick 

        # if it is odd, we want to increment + 1 due to edge case
        # if it is even, it should not matter

        # now we have to reverse this half 

        dummy = ListNode()
        answer = dummy

        middle_node = self.obtain_middle(head)
        reverse_list_pointer = self.reverse(middle_node)
        first_half_pointer = head

        while first_half_pointer and reverse_list_pointer:
            dummy.next = first_half_pointer
            first_half_pointer = first_half_pointer.next
            dummy = dummy.next
            dummy.next = reverse_list_pointer
            reverse_list_pointer = reverse_list_pointer.next
            dummy = dummy.next
        
        if first_half_pointer:
            dummy.next = first_half_pointer
        
        return answer.next

    def obtain_middle(self, head):
        middle, fast = head, head

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        slow = middle
        middle = middle.next
        slow.next = None
        return middle

    def reverse(self, middle_node):
        prev = None
        while middle_node:
            temp = middle_node.next
            middle_node.next = prev
            prev = middle_node
            middle_node = temp
        return prev
