class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stack;  // (index, temperature)
        vector<int> res(temperatures.size(), 0);  
        
        for (int i = 0; i < temperatures.size(); i++) {
            int t = temperatures[i];
            while (!stack.empty() && stack.top().second < t) {
                auto pair = stack.top();
                stack.pop();
                res[pair.first] = i - pair.first;
            }
            stack.push({i, t});
        }
        return res;
    }
};