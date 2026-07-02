class Solution:
    def isValid(self, s: str) -> bool:
        opening = '([{'
        closing = ')]}'
        list_brackets = []
        if len(s)==1:
            return False
        sol_dict = {')':'(',']':'[','}':'{'}
        for ch in s:
                if ch in opening:
                   list_brackets.append(ch)
                if ch in closing:
                    if list_brackets:
                        if sol_dict[ch] == list_brackets[-1]:
                           list_brackets.pop()
                        else:
                           return False
                    else: 
                        return False
        if not list_brackets:
            return True
        else:
            return False       
        
            
