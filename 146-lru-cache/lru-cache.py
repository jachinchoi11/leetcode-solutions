
# i think i started learning about this in my systems class, so it's gonna be interesting to do 
# so bascially, its a cache that wil favor least reacently used (so timewise), as the cache can't have infinte space
# let's start from the thing, so we add something to the cache 

    # and then we have to be able to get it, so maybe like a queue and a hashmap (key: to a value) 

    # but i just realized that what if we need to move something to the very top from the beginnign
        # we would have to index thorugh the entire thing O(n) everytime we put a value 
        # so i'm thinking that we use a differnet data sturcutre
            # i'm thinking we could potentily use a node (LinkedList)
                # singly or doubly not too sure - doubly lniedlist 
        
        # but basically we can have a ListNode() on one side - most recent
        # other side being - not used 

        # and i think we can just use the hashmap to point from the key to a value to a key --> node

        # so esssentially, if we do have a key and want to use the other key or put somethign new, we need to move it to to the very top 
            # so we need some type of remove and insert at top function 
                # remove () 
                # insert_front()

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.front = ListNode(None, None)
        self.back = ListNode(None, None)
        self.front.next = self.back
        self.back.prev = self.front
        self.capacity = capacity
        self.key_to_node = {}

    def get(self, key: int) -> int:
        
        if key in self.key_to_node:
            used_node = self.key_to_node[key]
            self.remove(used_node)
            self.insert_front(used_node)
            return used_node.val
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:

        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
        new_node = ListNode(key, value)
        self.key_to_node[key] = new_node
        self.insert_front(new_node)

        if len(self.key_to_node) > self.capacity:
            last_node = self.back.prev
            remove_key = last_node.key
            self.remove(last_node)
            self.key_to_node.pop(remove_key)


        # only time we remove somethign is when 


        # Case 1: we are under capacity --> we just add the key to the node and add to the most recent (new_node)
        # Case 2: we are under capacity --> soemthing is already ther efor the node so we have to remove and then add to the front (new_node)
            # Case 1,2 --> first check if the key is already there (remove if it is there)
            # Then add the node into the beginning 
        
        # Case 3 : we are over capacity --> so we remove the node that is pointed to by the right.prev

    def remove(self, node):
        # cuts out the node
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_front(self, node):
        first_node = self.front.next
        self.front.next = node
        node.prev = self.front
        node.next = first_node
        first_node.prev = node


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)