class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # essentially have a current count of the characters, make sure that before u add
        # the character before is added in terms of the index
            # tried to complicate it here and check just beofre when cpudln've checked as a whole
        currFrogs = 0
        maxFrogs = 0
        count = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}

        for char in croakOfFrogs:
            count[char] += 1
            if char == 'c':
                currFrogs += 1
                maxFrogs = max(currFrogs, maxFrogs)
            elif char == 'k':
                currFrogs -= 1
            
            if not (count['c'] >= count['r'] >= count['o'] >= count['a'] >= count['k']):
                # dont care about other ones but we do care that one comes befor ethe other 
                # check the general gist 
                return -1
        
        for value in count.values():
            if value != (len(croakOfFrogs) / 5):
                return -1
        
        return maxFrogs


