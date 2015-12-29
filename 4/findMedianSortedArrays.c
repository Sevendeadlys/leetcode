#define max(a, b)  (((a) > (b)) ? (a) : (b))
#define min(a, b)  (((a) < (b)) ? (a) : (b))
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int lo,hi,sum;
    int i,j;
    int a,b;

    if(nums1Size > nums2Size){
        return findMedianSortedArrays(nums2,nums2Size,nums1,nums1Size);
    }

    lo = 0;
    hi = nums1Size;
    sum = (nums1Size + nums2Size + 1)/2;

    while(lo <= hi){
        i = (lo + hi)/2;
        j = sum - i;

        if(j > 0 && i < nums1Size && nums1[i] < nums2[j - 1]){
            lo = i + 1;
        }
        else if(i > 0 && j < nums2Size && nums2[j] < nums1[i - 1]){
            hi = i - 1;
        }
        else{
            if(i == 0){
                a = nums2[j-1];
            }
            else if(j == 0){
                a = nums1[i-1];
            }
            else{
                a = max(nums2[j-1],nums1[i-1]);
            }

            if((nums1Size + nums2Size)%2 == 1){
                return a;
            }
            if(i == nums1Size){
                b = nums2[j];
            }
            else if(j == nums2Size){
                b = nums1[i];
            }
            else{
                b = min(nums2[j],nums1[i]);
            }
            return (double)((a+b)/2.0);
        }
    }
}
