class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        return sum([n for i, n in enumerate(nums) if i % 2 == 0])
        