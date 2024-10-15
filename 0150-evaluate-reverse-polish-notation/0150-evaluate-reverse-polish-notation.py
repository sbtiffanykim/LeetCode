class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        
        for token in tokens:
            if token in operators:
                val = 0
                second = stack.pop()
                first = stack.pop()
                if token == '+': val = first + second
                elif token == '-': val = first - second
                elif token == '*': val = first * second
                else: val = int(first / second)
                stack.append(val)
            else:
                stack.append(int(token))
        
        return stack[-1]