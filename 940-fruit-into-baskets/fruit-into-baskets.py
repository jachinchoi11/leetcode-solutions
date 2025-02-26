class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # you want to get the maximum amoutn of fruits (but only two types of fruit allowed)
        # so keep on going until you have two fruits max 


        curr_count = defaultdict(int)
        left, right, res, curr_amount = 0, 0, 0, 0

        while right < len(fruits):
            curr_fruit = fruits[right]
            curr_count[fruits[right]] += 1
            curr_amount += 1

            while len(curr_count) > 2:
                left_fruit = fruits[left]
                curr_count[left_fruit] -= 1
                if curr_count[left_fruit] == 0:
                    curr_count.pop(left_fruit)
                curr_amount -= 1
                left += 1
            res = max(res, curr_amount) 
            right += 1
        return res