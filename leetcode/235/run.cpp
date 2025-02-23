/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == p)
            return p;
        if (root == q)
            return q;
        int pval = p->val, qval = q->val, rval = root->val;
        // assuming p < q, if not, swap
        if (pval > qval) {
            std::swap(p, q);
            std::swap(pval, qval);
        }
        // diff sides of tree
        if (pval <= rval && qval >= rval) {
            return root;
        } else if (pval < rval && qval < rval) {
            return lowestCommonAncestor(root->left, p, q);
        } else {
            return lowestCommonAncestor(root->right, p, q);
        }

    }
};
