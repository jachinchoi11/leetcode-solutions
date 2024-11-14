class Solution:
    def digitCount(self, num: str) -> bool:
        count = defaultdict(int)
        for char in num:
            count[char] += 1
        print(count)
        for index in range(len(num)):
            if count[str(index)] != int(num[index]):
                return False
        return True