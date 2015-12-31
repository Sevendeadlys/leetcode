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

#define ARRAY_SIZE 50
#define REALLOC_SIZE 10
#define STACK_MALLOC(size) (struct TreeNode **)malloc(4*size)
#define STACK_REALLOC(stack,size) (struct TreeNode **)realloc(stack,4*size)
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int *result;
    int array_size;
    struct TreeNode **stack;
    int stack_size;
    int length;
    int index;
    struct TreeNode *temp;

    if(!root) return NULL;

    array_size = ARRAY_SIZE;
    result = (int*)malloc(array_size*sizeof(int));
    stack_size = ARRAY_SIZE;
    stack = STACK_MALLOC(stack_size);
    length = 0;
    index = 0;

    stack[length++] = root;

    while(length > 0)
    {
        if(index >= array_size)
        {
            array_size += REALLOC_SIZE;
            result = (int*)realloc(result, array_size*sizeof(int));
        }
        temp = stack[--length];
        result[index++] =  temp->val;

        if(temp->right) {
            if(length >= stack_size){
                stack_size += REALLOC_SIZE;
                stack = STACK_REALLOC(stack,stack_size);
            }
            stack[length++] = temp->right;
        }

        if(temp->left) {
            if(length >= stack_size){
                stack_size += REALLOC_SIZE;
                stack = STACK_REALLOC(stack,stack_size);
            }
            stack[length++] = temp->left;
        }
    }
    *returnSize = index;
    free(stack);
    return result;
}
