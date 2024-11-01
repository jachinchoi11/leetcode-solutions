class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for index, word in enumerate(words):
            if word in dictionary:
                if dictionary[word] != pattern[index]:
                    return False
            else:
                if pattern[index] in dictionary.values():
                    return False
                dictionary[word] = pattern[index]

        return True