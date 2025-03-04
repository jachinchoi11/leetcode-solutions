class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:

        """
        what you have to do is get the greatest damage that is bigger is less than or equal to armor 
        and then just add the rest up
        """
        curr_sum = 0
        max_level = 0
        for level in damage:
            if level > max_level:
                max_level = level
            curr_sum += level
        
        return curr_sum - armor + 1 if armor <= max_level else curr_sum - max_level + 1

