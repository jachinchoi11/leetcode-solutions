class Solution:
    def minDeletions(self, s: str) -> int:

        count = defaultdict(int)
        setFreq = set()

        deletions = 0
        for char in s:
            count[char] += 1
        
        for value in count.values():
            while value in setFreq:
                value -= 1
                deletions += 1
            setFreq.add(value)
            if 0 in setFreq:
                setFreq.remove(0)
        
        return deletions
