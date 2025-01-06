class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        answer = [0] * len(boxes)

        # i'm guessing we can have a hashamp that racks where all the i's are and we can make a helper function that essentially determines how far each element is away from the thign 

        def move_helper(index):
            res = 0
            for value in counter['1']:
                if value == index:
                    continue
                res += abs(value - index)
            return res
                
        
        # we have to first create the hashmap
        counter = defaultdict(list)
        for index, char in enumerate(boxes):
            if char == '1':
                counter[char].append(index)

        for curr_index in range(len(answer)):
            curr_number_of_moves = move_helper(curr_index)
            answer[curr_index] = curr_number_of_moves
        return answer
