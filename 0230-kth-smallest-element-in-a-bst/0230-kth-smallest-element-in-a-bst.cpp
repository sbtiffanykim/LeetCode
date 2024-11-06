/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> vals(2);  // {cnt, val}
        vals[0] = k;
        dfs(root, vals);
        return vals[1];
    }
    
    void dfs(TreeNode* node, vector<int> &vals) {
        if (!node) return;
        dfs(node->left, vals);
        vals[0]--;
        if (vals[0] == 0) {
            vals[1] = node->val;
            return;
        }
        dfs(node->right, vals);
    }
};