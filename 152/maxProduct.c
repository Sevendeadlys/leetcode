int maxProduct(int* nums, int numsSize) {
    if(numsSize < 1) return 0;
    int max = nums[0];
    int min = nums[0];
    int product = nums[0];
    
    for(int i = 1; i < numsSize; i++){
        if(nums[i] >= 0){
            max = max*nums[i] > nums[i]?max*nums[i]:nums[i];
            min = min*nums[i] < nums[i]?min*nums[i]:nums[i];
        }
        else{
            int temp = max;
            max = min*nums[i] > nums[i]?min*nums[i]:nums[i];
            min = temp*nums[i] < nums[i]?temp*nums[i]:nums[i];
        }
        product = product > max? product:max;
    }
    return product;
}