class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for word in strs:
            res += (f"{len(word)}#{word}")
        return res

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        pointer = 0
        res = []

        while pointer < len(s):
            index = s.find('#', pointer)

            length = int(s[pointer:index])
            pointer += (index-pointer) + 1
            word = s[pointer:pointer + length]
            pointer += length
            res.append(word)
        return res
        


        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))