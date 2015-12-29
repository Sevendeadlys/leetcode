/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isValidBST(struct TreeNode* root) {
    bool status = true;
    struct TreeNode ** stack = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * 50);
    int length;
    struct TreeNode * node;

    if(!root) return true;

    if(root->left){
        length = 0;
        stack[length++] = root->left;
        while(length > 0){
            node = stack[--length];
            if(node->val >= root->val) return false;

            if(node->right) stack[length++] = node->right;
            if(node->left) stack[length++] = node->left;
        }
    }

    if(root->right){
        length = 0;
        stack[length++] = root->right;
        while(length > 0){
            node = stack[--length];
            if(node->val <= root->val) return false;

            if(node->right) stack[length++] = node->right;
            if(node->left) stack[length++] = node->left;
        }
    }

    return (status && isValidBST(root->left) && isValidBST(root->right));
}
