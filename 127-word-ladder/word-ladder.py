class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # get closest to the place, or actually maybe we can start from the beginWord, as its hard t knpw

        # and then do a shortest path bfs from the beginWord to the endWord 

        connections = defaultdict(list)

        
        queue = deque()
        path = set()
        queue.append(beginWord)
        path.add(beginWord)
        res = 1

        while queue:
            for _ in range(len(queue)):
                currWord = queue.popleft()

                if currWord == endWord:
                    return res
                path.add(currWord)

                if currWord not in connections:
                    self.findConnections(currWord, connections, wordList)

                for connectedWord in connections[currWord]:
                    if connectedWord not in path:
                        queue.append(connectedWord)
            
            res += 1
        
        return 0
    

    def findConnections(self, findWord, connections, wordList):
        for word in wordList:
            diff = 0
            for index in range(len(word)):
                if word[index] != findWord[index]:
                    diff += 1
                    if diff >= 2:
                        break
            if diff <= 1 and diff > 0:
                connections[findWord].append(word)
        





        


                
                    



