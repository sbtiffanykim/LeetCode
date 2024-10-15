class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = list()
        match = {')': '(',  ']': '[', '}': '{'}
        for c in s:
            if c not in match.keys():  # open parenthesis
                stack.append(c)
            else:  # closed parenthesis
                # if there isn't any open parenthesis or parenthesis does not match
                if not stack or stack[-1] != match[c]:
                    return False
                stack.pop()
        
        return False if stack else True
        