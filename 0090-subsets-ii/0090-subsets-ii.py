class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the nums to help with pruning
        
        def backtrack(idx, subset):
            if idx == len(nums):
                res.append(subset[:])
                return
        
            # All subsets include nums[i]
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()
            
            # All subsets that don't include nums[i]
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, subset)
        
        backtrack(0, [])
        return res