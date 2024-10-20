class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # if the portion is already fully sorted
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = left + (right - left) // 2
            # update the min value(=res)
            res = min(res, nums[mid])
            if nums[mid] < nums[left]:
                right = mid - 1
            else: 
                left = mid + 1
        
        return res