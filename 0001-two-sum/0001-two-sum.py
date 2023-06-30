class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            if target-n in nums[idx+1:]:
                return [idx, nums[idx+1:].index(target-n)+(idx+1)]
        