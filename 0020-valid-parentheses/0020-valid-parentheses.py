class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')': '(', '}': '{', ']': '['}
        stack = list()
        
        for c in s:
            if c not in parentheses:
                stack.append(c)
            elif not stack or stack.pop() != parentheses[c]:
                return False
        
        return (len(stack) == 0)