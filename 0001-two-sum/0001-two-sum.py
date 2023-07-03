class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = collections.defaultdict()
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return [idx, nums_dict[diff]]
            nums_dict[num] = idx