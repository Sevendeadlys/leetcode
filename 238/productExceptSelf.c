/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int right;
    int *returnArray = (int*)malloc(numsSize*sizeof(int));

    *returnSize = numsSize;

    returnArray[0] = 1;
    right = 1;
    for(int index = 1; index < numsSize; index++)
        returnArray[index] = returnArray[index-1]*nums[index-1];

    for(int index = numsSize - 1; index > -1; index--)
    {
        returnArray[index] *= right;
        right *= nums[index];
    }
    return returnArray;
}
