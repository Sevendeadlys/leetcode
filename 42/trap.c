/*
Indeed this question can be solved in one pass and O(1) space,
but it's probably hard to come up with in a short interview.
If you have read the stack O(n) solution for Largest Rectangle in Histogram,
you will find this solution is very very similar.

The main idea is : if we want to find out how much water on a bar(bot),
we need to find out the left larger bar's index (il), and right larger bar's index(ir),
so that the water is (min(A[il],A[ir])-A[bot])*(ir-il-1),
use min since only the lower boundary can hold water,
and we also need to handle the edge case that there is no il.

To implement this we use a stack that store the indices with decreasing bar height,
once we find a bar who's height is larger, then let the top of the stack be bot,
 the cur bar is ir, and the previous bar is il.
*/
int trap(int* height, int heightSize) {
    int *stack = (int*)malloc(4*heightSize);
    int sp = 0;
    int i = 0;
    int res = 0;

    while(i<heightSize){
        if(sp == 0 || height[i] <= height[stack[sp-1]]){
            stack[sp++] = i++;
        }
        else{
            int bot = stack[--sp];
            if(sp != 0){
                int min = height[stack[sp-1]]>height[i]?height[i]:height[stack[sp-1]];
                res += (min-height[bot])*(i-stack[sp-1]-1);
            }
        }
    }
    free(stack);
    return res;
}
