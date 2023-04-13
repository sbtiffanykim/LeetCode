class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacked_s = list()
        stacked_t = list()
        
        for char in s:
            if char != "#": stacked_s.append(char)
            else: 
                if len(stacked_s) > 0: stacked_s.pop()
        
        for char in t:
            if char != "#": stacked_t.append(char)
            else: 
                if len(stacked_t) > 0: stacked_t.pop()
        
        return True if stacked_s == stacked_t else False
        