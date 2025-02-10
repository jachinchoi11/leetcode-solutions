class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # we can use somethign like a stack data strucutre 
        # where we can maybe pop off the latest thing, we can treat it as if we carry the /char as each thign
        # when we see the .., we can pop off what we have arledy seen
        # maybe we can just pop off of it

        # if the split res has nothing in it just continue
            # this makes up for the // and /// cases

        
        # if it is ever ..  --> you pop
        # and if 

        parsed_path = path.split('/')
        res = []
        for char in parsed_path:
            if char == "" or char == '.':
                continue
            else:
                if char == "..":
                    if res:
                        res.pop()
                else:
                    res.append(char)
        
        final_ans = "/".join(res)
        return '/' + final_ans
            

            