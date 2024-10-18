class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());
        int res = right;
        
        while (left <= right) {
            int k = left + (right - left) / 2;
            long long total = 0;
            // calculate time taken to eat all
            for (int pile: piles) {
                total += ceil(static_cast<double>(pile) / k);
            }
            if (total <= h) {
                res = k;
                right = k - 1;
            } else {
                left = k + 1;
            }
        }
        return res;
    }
};