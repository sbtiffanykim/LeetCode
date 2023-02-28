class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        min_n = min(nums)
        max_n = max(nums)
        # to record the previous index of the list
        temp = 0
        # to record an index of a previous digit
        left = 0
        for n in range(min_n, max_n):
            try:
                # find the first occurrence of the next digit 
                next_idx = nums.index(n+1)
                # insert the digit
                temp += 1
                nums[temp] = n+1
                left = next_idx
                k += 1
            # if there the next digit does not exist
            except ValueError:
                continue
        if temp+1 < len(nums):
            nums[temp+1] = max_n
        return k