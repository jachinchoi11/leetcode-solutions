class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        ans = []

        for index, char in enumerate(s):
            if char not in '()':
                continue
            if char == ')':
                if stack:
                    stack.pop()
                else:
                    res.append(index)
            else:
                stack.append(index)
                # track the indexes
        while stack:
            res.append(stack.pop())
        print(res)
        for index in range(len(s)):
            if index in res:
                continue
            else:
                ans.append(s[index])
        return "".join(ans)
        

