/*
* the varietas for binary search
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int lo,hi,mid;
    int *result = (int*)malloc(sizeof(int)*2);

    if(numsSize == 0) return NULL;
    result[0] = -1;
    result[1] = -1;
    *returnSize = 2;

    lo = 0;
    hi = numsSize - 1;
    while(lo <= hi){
        mid = (lo + hi)/2;
        if(nums[mid] >= target){
            hi = mid - 1;
        }
        else{
            lo = mid + 1;
        }
    }
    if(nums[lo] != target){
        return result;
    }
    result[0] = lo;

    lo = 0;
    hi = numsSize - 1;
    while(lo <= hi){
        mid = (lo + hi)/2;
        if(nums[mid] <= target){
            lo = mid + 1;
        }
        else{
            hi = mid - 1;
        }
    }
    result[1] = hi;
    return result;
}
