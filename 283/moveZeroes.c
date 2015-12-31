void moveZeroes(int* nums, int numsSize) {
    int index = 0;
    int h_zero_index = -1;
    int t_zero_index = -1;

    if(numsSize < 2) return;

    while((index < numsSize) && (nums[index] != 0)) index++;

    if(index == numsSize) return;

    h_zero_index = index;
    t_zero_index = index;

    index = index + 1;
    for(;index < numsSize;index++)
    {
        if(nums[index] == 0)
        {
            t_zero_index = index;
        }
        else
        {
            nums[h_zero_index] = nums[index];
            nums[index] = 0;
            h_zero_index ++;
            t_zero_index = index;
        }
    }
    return;
}
