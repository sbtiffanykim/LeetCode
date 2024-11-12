class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(nums, 0, path, res);
        return res;
    }
private:
    void dfs(vector<int>& nums, int idx, vector<int>& path, vector<vector<int>>& res) {
        if (idx >= nums.size()) {
            res.push_back(path);            
            return;
        }
        // decision to include nums[i]
        path.push_back(nums[idx]);
        dfs(nums, idx+1, path, res);
        
        // decision not to include nums[i]
        path.pop_back();
        dfs(nums, idx+1, path, res);
    }
};