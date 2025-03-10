class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # so we're given two words and a beginWord endWord
            # we can only use the words in teh word list to change it 

            # i think one thing we can do is to start with the beginning word
                # make an adj list
                # go through all the words and see if they only have a one letter difference to switch
                # make a helper that will go through that and edit the adj list 
            
                # and then just add that into the bfs and keep on doing that until i hit final word

        queue = deque([beginWord])
        adj_list = defaultdict(list)
        res = 1
        visited = set()

        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                visited.add(curr_word)
                if curr_word == endWord:
                    return res
                
                if curr_word not in adj_list:
                    self.find_connections(curr_word, wordList, adj_list)
                
                for neighbor in adj_list[curr_word]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            res += 1
        return 0

    def find_connections(self, curr_word, wordList, adj_list):

        for word in wordList:
            changes = 0
            for index in range(len(word)):
                if curr_word[index] != word[index]:
                    changes += 1
                if changes == 2:
                    break
            if changes < 2:
                adj_list[curr_word].append(word)
