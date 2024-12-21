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
    bool is_in_range(int x, std::optional<int> l, std::optional<int> r) {
        bool b = true;
        if (l.has_value()) {
              b = b && (x > l.value());
        }
        if (r.has_value()) {
              b = b && (x < r.value());
        }
        return b;
    }
    bool isValidBST(TreeNode* root) {
        if (root == nullptr)
            return true;
        return helper(root->left, {std::optional<int>{}, root->val}, true) && helper(root->right, {root->val, std::optional<int>{}}, false);
        
    }
    bool helper(TreeNode* root, std::pair<std::optional<int>, std::optional<int>> range, bool is_left) {
    if (root == nullptr) {
        return true;
    } else {
        auto lrange = range.first;
        auto rrange = range.second;
        if (is_in_range(root->val, lrange, rrange)) {
            std::pair<std::optional<int>, std::optional<int>> newrange_left{lrange,std::optional<int>{root->val}};
            std::pair<std::optional<int>, std::optional<int>> newrange_right{std::optional<int>{root->val},rrange};
            return helper(root->left, newrange_left, true) && helper(root->right, newrange_right, false);
        } else {
            return false;
        }
    }
}

};
