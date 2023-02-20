class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            digits = 0
            num = nums[i]
            while num > 0:
                num = num // 10
                digits += 1
            if digits % 2 == 0:
                answer += 1
        return answer
