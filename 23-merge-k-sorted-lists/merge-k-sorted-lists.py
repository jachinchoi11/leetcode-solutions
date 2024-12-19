# Definition for singly-linked list.
class HeapNode:
    def __init__(self, node,val=0, next=None):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # you have k linked lisrts 
        # you can essentially have a pointer to the values and compare the pointers and make the ListNode
        dummy = ListNode(0)
        prev = dummy
        heap = []
            
        for currList in lists:
            if currList:
                heapq.heappush(heap, HeapNode(currList))
        
        while heap:
            address = heapq.heappop(heap)
            node = address.node
            if node.next:
                nextNode = node.next
                heapq.heappush(heap, HeapNode(nextNode))
            dummy.next = node
            dummy = dummy.next
        return prev.next
        