/**
 * calculate all the two sum in array
 * return the sum which equals to target
 * the time O(n^2)
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *ret = (int*)malloc(sizeof(int)*2);
    
    for(int i = 0; i < numsSize; i++){
        for(int j = i + 1; j < numsSize; j++){
            int sum = nums[i] + nums[j];
            if(sum == target){
                ret[0] = i + 1;
                ret[1] = j + 1;
                return ret;
            }
        }
    }
    return NULL;
}