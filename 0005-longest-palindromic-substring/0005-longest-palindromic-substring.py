class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check if the given string is palindromic & expand two pointers
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                # expand the pointers
                left -= 1
                right += 1
            return s[left + 1 : right - 1]
        
        answer = ''  # the longest palindromic substring
        
        if len(s) == 1 or s == s[::-1]:
            return s
        
        for i in range(len(s) - 1):
            # consider both cases: odd(i, i+2) / even(i, i+1) palindrome
            answer = max(answer, expand(i, i + 1), expand(i, i + 2), key=len)  # longest palindrome 

        return answer
