class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        parseSentence = sentence.split()
        hashset = set(dictionary)
        
        for index in range(len(parseSentence)):
            currWord = parseSentence[index] 
            for right in range(len(currWord) + 1):
                if currWord[0:right] in hashset:
                    parseSentence[index] = currWord[0:right]
                    break
            
        

        return " ".join(parseSentence)

            
