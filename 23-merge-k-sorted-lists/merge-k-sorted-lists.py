# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        heap = []

        dummy = ListNode(0)
        answer = dummy

        for index, curr_list in enumerate(lists):
            if curr_list:
                heapq.heappush(heap, (curr_list.val, index, curr_list))
                curr_list = curr_list.next
        
        while heap:

            _, curr_index, min_node = heapq.heappop(heap)

            dummy.next = min_node
            dummy = dummy.next
        
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, curr_index, min_node.next))
                min_node = min_node.next
        return answer.next

        