class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group;
        for (const auto &s: strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            group[sortedS].push_back(s);
        }
        vector<vector<string>> res;
        for (auto &pair: group) {
            res.push_back(pair.second);
        }
        return res;
    }
};