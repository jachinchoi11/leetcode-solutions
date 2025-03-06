# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # merge all the sorted linked lists and put them all together 

        # so i thin ka great way to do this is knowing that they all are sorted, we could just move all the values into a heap 
        # and then just pop them off and form it that way

        # or we can maybe do a copmarison for each of the nodes, so we'll have a pointer from each of the lists, and then we'll get one thing from each place
        # so essetnailly, pointers for all of them,to keep track of them, we can have thier value - first, row and column, and then the ListNode()
        
        # if they are the same 
            # then we can just take whateer, doesnt matter
        rows = len(lists)
        heap = []
        dummy_node = ListNode()
        prev = dummy_node

        for row in range(rows):
            # we're building our initial heap 
            if lists[row]:
                heapq.heappush(heap, (lists[row].val, row, lists[row]))
                lists[row] = lists[row].next
            
        
        while heap:
            # this would be self sufifcient, because we woudl always try to add more if there is 
            # we can not index through this 
            _, curr_row, curr_node = heapq.heappop(heap)
            dummy_node.next = curr_node
            dummy_node = dummy_node.next

            if lists[curr_row]:
                heapq.heappush(heap, (lists[curr_row].val, curr_row, lists[curr_row]))
                lists[curr_row] = lists[curr_row].next

        return prev.next
            
            

        