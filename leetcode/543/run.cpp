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
    int depth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        } else {
            return 1+max(depth(root->left), depth(root->right));
        }
    }

    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        } else {
            auto l = depth(root->left) - 1;
            auto r = depth(root->right) - 1;
            auto diameter_with_root = l + 2 + r;
            auto dl = diameterOfBinaryTree(root->left);
            auto dr = diameterOfBinaryTree(root->right);

            return dr > dl ? (dr > diameter_with_root ? dr : diameter_with_root) : (dl > diameter_with_root ? dl : diameter_with_root);
        }
        
    }
};
