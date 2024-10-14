class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        if nums[0] > 0 or len(nums) < 3: return result # bad cases
        
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: continue  # ignore any duplicates
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                curSum = val + nums[left] + nums[right]
                if curSum > 0:
                    right -= 1
                elif curSum < 0:
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # ignore any duplicates
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # ignore any duplicates
                        right -= 1
                    left += 1  # increment the left pointer
                    right -= 1  # decrement the right pointer
        
        return result