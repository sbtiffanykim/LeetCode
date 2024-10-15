class Solution {
public:
    bool isValid(string s) {
        stack<char> open;
        unordered_map<char, char> match = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        for (const auto &c: s) {
            // opened parenthesis
            if (match.find(c) == match.end()) {
                open.push(c);
            } else {
                if (open.empty()) return false;  // opened parenthesis does not exist
                if (open.top() != match[c]) return false;  // parenthesis does not match
                open.pop();
            }
        }
        return open.empty();
    }
};