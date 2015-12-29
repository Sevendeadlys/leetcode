/*
* the varietas for binary search
*/
int searchInsert(int* nums, int numsSize, int target) {
    int low,high,mid;

    low = 0;
    high = numsSize - 1;

    while(low <= high)
    {
        mid = (low + high) / 2;
        int temp = nums[mid];
        if(temp > target){
            high = mid - 1;
        }
        else if(temp < target){
            low = mid + 1;
        }
        else
        {
            return mid;
        }
    }
    return low;
}
