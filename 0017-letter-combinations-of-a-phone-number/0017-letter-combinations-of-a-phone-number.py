class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_to_char = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res, path = [], []
        
        def dfs(i: int, path: List[str]):
            if i == len(digits):
                res.append(''.join(path[:]))
                return
            
            for j in dig_to_char[digits[i]]:
                path.append(j)
                dfs(i + 1, path)
                path.pop()
        
        if len(digits) > 0:
            dfs(0, [])
        return res
                