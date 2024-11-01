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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        deque<TreeNode*> queue;
        if (root) queue.push_back(root);
        
        while (!queue.empty()) {
            vector<int> curLevel;  // Initialize current level vector
            int level_size = queue.size();  // Get number of nodes at current level
            
            for (int i = 0; i < level_size; i++) {
                TreeNode* curNode = queue.front();
                queue.pop_front();
                curLevel.push_back(curNode->val);
                
                if (curNode->left) queue.push_back(curNode->left);
                if (curNode->right) queue.push_back(curNode->right);
            }
            res.push_back(curLevel);
        }
        return res;
    }
};