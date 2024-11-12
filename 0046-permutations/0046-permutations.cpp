class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> path;
        vector<bool> picked(nums.size(), false);
        backtrack(nums, path, picked);
        return res;
    }
    
    void backtrack(vector<int>& nums, vector<int>& path, vector<bool>& picked) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        
        for (int i = 0 ; i < nums.size(); i++) {
            if (!picked[i]) {
                path.push_back(nums[i]);
                picked[i] = true;
                backtrack(nums, path, picked);
                path.pop_back();  // Backtracking
                picked[i] = false;
            }
        }
    }
};