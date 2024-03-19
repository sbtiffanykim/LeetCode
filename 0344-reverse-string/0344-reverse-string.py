class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1  # use two pointers
        while left < right:
            s[left], s[right] = s[right], s[left]  # swap two characters
            left += 1
            right -= 1
        