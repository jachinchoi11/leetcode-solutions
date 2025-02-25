class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]: 

        # in this case, we will not count down because we need to have the exact amount
        # so we will have a current counter for the character -> to the hashmap

        word_length = len(words[0])
        curr_count = defaultdict(int)
        counter_ans = Counter(words)
        res = []
        for curr_index in range(word_length):
            left, right = curr_index, curr_index
            curr_count.clear()
            curr_matches = 0
            while right + word_length <= len(s):
                curr_string = s[right:right + word_length]
                right += word_length

                if curr_string in counter_ans:
                    curr_count[curr_string] += 1
                    if curr_count[curr_string] == counter_ans[curr_string]:
                        curr_matches += 1
                
                    while curr_count[curr_string] > counter_ans[curr_string]:
                        left_string = s[left: left + word_length]
                        curr_count[left_string] -= 1
                        if curr_count[left_string] == counter_ans[left_string] - 1:
                            curr_matches -= 1
                        left += word_length
                else:
                    left = right
                    curr_count.clear()
                    curr_matches = 0
                
                if curr_matches == len(counter_ans):
                    res.append(left)
            right += word_length
        return res


        







