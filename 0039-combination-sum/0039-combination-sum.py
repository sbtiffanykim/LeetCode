class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, cur_candidates, cur_sum) -> None:
            # If the sum is eqaul to the target, add the candidate to the result
            if cur_sum == target:
                result.append(cur_candidates[:])
            # If the sum exceeds the target, stop exploring the path
            elif cur_sum > target:
                return
            
            for i in range(idx, len(candidates)):
                cur_candidates.append(candidates[i])
                dfs(i, cur_candidates, cur_sum + candidates[i])  # Recursive with the updated sum
                cur_candidates.pop()  # Backtracking
        
        result = []
        candidates.sort()  # Pruning
        dfs(0, [], 0)
        return result