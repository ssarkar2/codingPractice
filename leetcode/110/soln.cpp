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

    pair<bool, int> helper(TreeNode* root) {
        if (root==nullptr)
            return {true, 0};
        
        auto [l_balanced, l_height] = helper(root->left);
        if (!l_balanced)
            return {false, 0};
        auto [r_balanced, r_height] = helper(root->right);
        return {l_balanced && r_balanced && (std::abs(l_height-r_height) <= 1), std::max(l_height, r_height) + 1};
    }
    bool isBalanced(TreeNode* root) {
        return helper(root).first;
    }
};
