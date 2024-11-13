class Solution {
public:
    vector<vector<int>> res;
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        backtrack(0, path, 0, candidates, target);
        return res;
    }

private:
    void backtrack(int i, vector<int> path, int curSum, vector<int>& candidates, int target) {
        if (curSum == target) {
            res.push_back(path);
            return;
        }
        if (i == candidates.size() || curSum > target) return;
        
        // include candidates[i]
        path.push_back(candidates[i]);
        backtrack(i+1, path, curSum + candidates[i], candidates, target);
        path.pop_back();
            
        // skip candidates[i]
        while (i + 1 < candidates.size() && candidates[i] == candidates[i+1]) i++;
        backtrack(i+1, path, curSum, candidates, target);
    }
};