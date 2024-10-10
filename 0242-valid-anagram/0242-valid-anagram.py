class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chr_in_s = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        chr_in_t = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        
        for c in s:
            chr_in_s[c] += 1
        for c in t:
            chr_in_t[c] += 1
        
        for c in range(ord('a'), ord('z') + 1):
            target = chr(c)
            if chr_in_s[target] != chr_in_t[target]:
                return False
        return True