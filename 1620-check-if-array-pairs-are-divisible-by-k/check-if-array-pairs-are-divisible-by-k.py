class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        # i think we can have a hashmap that will show what the pairs are 
            # the way we can take advantage of the hashamp approach is using the k to mod it 
            # and see what we woudl need 

        # res = 0 --> should equal the len(arr) // 2

        divisors = defaultdict(int)

        for num in arr:
            converted_num = num % k
            divisors[converted_num] += 1
        
        for key, value in divisors.items():
            target_divisor = k - key
            if key == target_divisor or key == 0:
                if divisors[key] % 2 != 0:
                    return False
            else:
                if target_divisor in divisors:
                    if value != divisors[target_divisor]:
                        return False
                else:
                    return False
        return True
