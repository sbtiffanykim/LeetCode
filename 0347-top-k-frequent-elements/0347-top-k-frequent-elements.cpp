class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num: nums) {
            count[num]++;
        }

        vector<pair<int, int>> sortedC;
        for (const auto& p: count) {
            sortedC.push_back({p.second, p.first});  // {frequency, number}
        }
        sort(sortedC.rbegin(), sortedC.rend());

        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(sortedC[i].second);
        }
        return res;
    }
};