/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int x, int y)
{
    return (x>y?x:y);
}
int maxDepth(struct TreeNode* root) {
    if(!root) return 0;

    return max(1+maxDepth(root->left),1+maxDepth(root->right));
}
