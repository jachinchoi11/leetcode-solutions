class Solution:
    def isValid(self, s: str) -> bool:

        # so here i think maybe we can use a stack in this case

        # using a stack will allow us to keep track of which things we do have, and i was thinking 
        # we just have store the open parentheses and then we can i guess pop it off if the same closing parentehse os there

        # any time we deviate would be 
            # when a closing bracket doesn't match --> immediately false
            # when there is a closing bracket, but no openign --> immediatly false -->check
            # also at the end if we have any opening ones that were'nt matched up --> false
                # else True
        # in terms of clarifyign questions, can we expect taht tehre will only be parenthese? 
            # what about will there always be an openign brakcet first? 
            # what do we do --> if there are other things --> skip

        

        stack = []

        match_map = {')' : '(', '}' : '{', ']': '['}

        for paren in s:

            if paren in ')]}':
                if stack and stack[-1] == match_map[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)
        
        return True if not stack else False

                




