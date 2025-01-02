class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        preCompute = [0] * (len(words))

        # we can precompute that amount of vowels in the range from where you are at to the beginning
        # and then we can just proces the queries using that
        currSum = 0
        hashset = set('aeiou')

        for index in range(len(words)):
            word = words[index]
            beginning = word[0]
            end = word[-1]
            if beginning in hashset and end in hashset:
                currSum += 1
            preCompute[index] = currSum

        for index, query in enumerate(queries):
            start, end = query
            if start == 0:
                res[index] = preCompute[end]
            else:
                res[index] = preCompute[end] - preCompute[start - 1]
        
        return res
