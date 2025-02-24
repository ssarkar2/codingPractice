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
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr)
            return {};
        auto left_ans = rightSideView(root->left);
        auto right_ans = rightSideView(root->right);
        vector<int> result;
        result.push_back(root->val);
        result.insert(result.end(), right_ans.begin(), right_ans.end());
        if (left_ans.size() > right_ans.size()) {
            result.insert(result.end(), left_ans.begin() + right_ans.size(), left_ans.end());
        }
        return result;
    }
};
