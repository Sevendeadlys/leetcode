/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define ARRAY_SIZE 100
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int *result;
    int array_size;
    struct TreeNode **stack;
    int stack_size;
    int length;
    int index;
    struct TreeNode *node;

    if(!root) return NULL;

    array_size = ARRAY_SIZE;
    result = (int*)malloc(array_size*sizeof(int));

    stack_size = ARRAY_SIZE;
    stack = (struct TreeNode **)malloc(sizeof(struct TreeNode *)*stack_size);

    length = 0;
    index = 0;

    node = root;

    while(node || length > 0){
        while(node){
            stack[length++] = node;
            node = node->left;
        }
        node = stack[--length];
        result[index++] = node->val;
        node = node->right;
    }

    *returnSize = index;
    free(stack);
    return result;
}
