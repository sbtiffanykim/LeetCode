class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        // bad cases
        if (nums[0] > 0 || n < 3) {
            return {};
        }
        
        for (int i = 0; i < n; i++) {
            int left = i + 1, right = n - 1;
            // ignore any duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            while (left < right) {
                int curSum = nums[i] + nums[left] + nums[right];
                if (curSum > 0) right--;
                else if (curSum < 0) left++;
                else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    while (left < right && nums[left] == nums[left + 1]) left++;  // ignore any duplicates
                    while (left < right && nums[right] == nums[right - 1]) right--;  // ignore any duplicates
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
};