class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        // binary search - row
        int top = 0;
        int bot = rows - 1;
        while (top <= bot) {
            int mid = top + (bot - top) / 2;
            if (matrix[mid][cols - 1] < target) {
                top = mid + 1;
            } else if (matrix[mid][0] > target) {
                bot = mid - 1;
            } else {
                break;
            }
        }
        
        if (!(top <= bot)) return false;  // none of the rows contain the target
        int row = (top + bot) / 2;  // the target row
        
        // binary search - column
        int left = 0;
        int right = cols - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (matrix[row][mid] < target) {
                left = mid + 1;
            } else if (matrix[row][mid] > target) {
                right = mid - 1;
            } else {
                return true;  // target exists
            }
        }
        return false;
    }
};