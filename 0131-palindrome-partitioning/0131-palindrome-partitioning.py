class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, cur = [], []
        
        def dfs(i: int) -> None:
            if i >= len(s):
                res.append(cur[:])
                return
            
            # Recursively search with backtracking
            for j in range(i, len(s)):
                if self.isPalindromic(s, i, j):
                    cur.append(s[i : j + 1])
                    dfs(j + 1)
                    cur.pop()
        
        dfs(0)
        return res
    
    
    # To check if the string is palindromic
    def isPalindromic(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
            