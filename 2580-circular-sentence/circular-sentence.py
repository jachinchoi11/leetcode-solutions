class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[len(sentence) - 1]:
            return False
        for index in range(len(sentence)):
            if sentence[index] == " ":
                if sentence[index - 1] != sentence[index + 1]:
                    return False
        return True