class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev, nxt = 0, 1  # using two pointers
        if len(nums) == 1:
            return False
        
        while True:
            if nums[prev] == nums[nxt]:  # if two adjancent numbers are identical
                return True
            # increase the pointers
            prev += 1 
            nxt += 1
            if nxt == len(nums):  # when nxt pointer reaches to the end of the array
                return False
