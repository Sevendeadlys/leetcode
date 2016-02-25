/*
1. Start from its last element, traverse backward to find the first one with index i that satisfy num[i-1] < num[i].
   So, elements from num[i] to num[n-1] is reversely sorted.
2. To find the next permutation, we have to swap some numbers at different positions,
   to minimize the increased amount, we have to make the highest changed position
   as high as possible. Notice that index larger than or equal to i is not possible
   as num[i,n-1] is reversely sorted. So, we want to increase the number at index i-1,
   clearly, swap it with the smallest number between num[i,n-1] that is larger than num[i-1].
   For example, original number is 121543321, we want to swap the '1' at position 2
   with '2' at position 7.
3. The last step is to make the remaining higher position part as small as possible,
   we just have to reversely sort the num[i,n-1]
*/
void reverse(int* nums,int s,int e){
    while(s < e){
        int temp = nums[s];
        nums[s] = nums[e];
        nums[e] = temp;
        s++;
        e--;
    }
}
void nextPermutation(int* nums, int numsSize) {
    if(numsSize < 2) return nums;
    int pos = numsSize - 1;
    int right = numsSize - 1;

    while(pos > 0 && nums[pos] <= nums[pos-1]) pos--;
    if(pos == 0) {
        reverse(nums,0,numsSize-1);
        return;
    }
    while(right >= pos && nums[right] <= nums[pos-1]) right--;
    int temp = nums[pos-1];
    nums[pos-1] = nums[right];
    nums[right] = temp;
    reverse(nums,pos,numsSize-1);
    return;
}
