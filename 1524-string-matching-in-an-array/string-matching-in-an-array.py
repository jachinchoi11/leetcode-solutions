class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        hashset = set()

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j or words[i] in hashset:
                    continue
                if words[i] in words[j]:
                    hashset.add(words[i])
        
        return list(hashset)