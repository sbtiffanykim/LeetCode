class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for idx, num in enumerate(nums):
            nums_dict[num] = idx
        
        for idx, num in enumerate(nums):
            if target-num in nums_dict and nums_dict[target-num] != idx:
                return [idx, nums_dict[target-num]]
        