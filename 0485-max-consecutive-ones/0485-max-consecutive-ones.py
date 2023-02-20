class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        temp = 0
        prev = nums[0]
        if prev == 1: temp += 1
            
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur == 1:
                temp += 1
            if cur == 0:
                answer = max(temp, answer)
                temp = 0
            prev = cur
        answer = max(temp, answer)
        return answer