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
    int diameterOfBinaryTree(TreeNode* root) {
        int longest = 0;
        dfs(root, longest);
        return longest;
    }
private:
    int dfs(TreeNode* node, int& longest) {
        if (!node) return 0;
        int left = dfs(node->left, longest);
        int right = dfs(node->right, longest);
        longest = max(longest, left + right);
        return 1 + max(left, right);
    }
};