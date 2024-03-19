import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-z]', '', s)  # remove all non-alphanumeric characters
        return s == s[::-1]