class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(idx: int, path: List[int], cur_sum: int) -> None:
            if cur_sum == target:
                res.append(path[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:  # Skip the duplicates
                    continue
                if cur_sum + candidates[i] > target:
                    break
                    
                path.append(candidates[i])
                backtrack(i + 1, path, cur_sum + candidates[i])
                path.pop()
            
        candidates.sort()        
        backtrack(0, [], 0)
        return res        