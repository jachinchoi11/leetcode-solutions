class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # what exactly are anagrams --> so we can rearrange them in any order possible 
        # we need to find a way to group them together essentially 
            # and we're groupiung them by soem common key
                # i think what would be common is if we were to sort the strings --> it would all go to the same thign 
                    # for example : nat and tan
                            # ant, ant
                            # so maybe that would work as the key 
                # the time comeplxity of the sort would be Nlogk 
        
        # we can use a ahsh,ap to map (sorted chars) : lists
            # and then output it

        sorted_to_answer = defaultdict(list)

        for word in strs:
            curr_key = tuple(sorted(word)) # sort only works for lists 
            sorted_to_answer[curr_key].append(word)
        
        return list(sorted_to_answer.values())


