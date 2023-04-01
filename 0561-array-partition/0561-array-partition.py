class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = sum([num for idx, num in enumerate(nums) if idx % 2 == 0])
        return answer