int maxSubArray(int* nums, int numsSize) {
    if(numsSize < 1) return 0;
    int sum = 0;
    int max = nums[0];
    
    for(int i = 0; i < numsSize; i++){
        sum += nums[i];
        max = max>sum?max:sum;
        if(sum < 0){
            sum = 0;
        }
    }
    return max;
}