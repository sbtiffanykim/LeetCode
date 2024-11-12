class Solution:
    def _backtrack(self, nums: List[int], path: List[int], picked: List[bool]) -> None:
        if len(path) == len(nums):
            self.result.append(path[:])
            return
        
        for i in range(len(nums)):
            if not picked[i]:
                path.append(nums[i])
                picked[i] = True
                self._backtrack(nums, path, picked)
                path.pop()  # Backtracking
                picked[i] = False
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []           
        self._backtrack(nums, [], [False] * len(nums))
        return self.result