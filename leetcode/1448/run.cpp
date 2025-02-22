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

    int helper(TreeNode* root, int maxval) {
        if (root == nullptr)
            return 0;
        auto currval = root->val;
        int counter{0};
        if (maxval <= currval) {
            counter += 1;
            maxval = currval;
        }
        counter += helper(root->left, maxval);
        counter += helper(root->right, maxval);
        return counter;

    }
    int goodNodes(TreeNode* root) {
        return root==nullptr ? 0 : 1 + helper(root->left, root->val) + helper(root->right, root->val);
    }
};
