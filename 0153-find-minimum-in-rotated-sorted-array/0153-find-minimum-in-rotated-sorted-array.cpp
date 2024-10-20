class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        int res = nums[0];
        
        while (left <= right) {
            // if the portion is already sorted
            if (nums[left] < nums[right]) {
                res = min(res, nums[left]);
                break;
            }
            int mid = left + (right - left) / 2;
            // update the min value
            res = min(res, nums[mid]);
            if (nums[mid] < nums[left]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }
};