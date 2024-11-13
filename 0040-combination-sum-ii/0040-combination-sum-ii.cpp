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
        
        for (int j = i; j < candidates.size(); j++) {
            if (j > i && candidates[j] == candidates[j-1]) continue;
            if (curSum + candidates[j] > target) break;
            
            path.push_back(candidates[j]);
            backtrack(j+1, path, curSum + candidates[j], candidates, target);
            path.pop_back();
        }
    }
};