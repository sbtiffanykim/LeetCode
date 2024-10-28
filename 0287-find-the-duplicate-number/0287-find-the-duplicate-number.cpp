class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // binary search
        int left = 1;
        int right = nums.size() - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            
            // Count the numbers less than or equal to mid
            for (int num: nums) {
                if (num <= mid) {
                    count++;
                }
            }
            
            // If the repeated number exist left to the mid
            if (count > mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
};