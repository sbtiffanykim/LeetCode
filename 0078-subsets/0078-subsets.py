class Solution:
    def _dfs(self, nums, index, path, res) -> None:
        # Add the current path to the result
        res.append(path.copy())
        
        # Explore all possible subsets starting from the current index
        for i in range(index, len(nums)):
            path.append(nums[i])
            self._dfs(nums, i + 1, path, res)
            path.pop()  # Backtracking

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self._dfs(nums, 0, [], res)
        return res

