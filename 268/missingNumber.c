int missingNumber(int* nums, int numsSize) {
    int index = 0;
    int ret = numsSize;

    for(index = 0;index < numsSize;index++)
    {
        ret ^= index;
        ret ^= nums[index];
    }
    return ret;
}
