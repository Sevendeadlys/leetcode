/*Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
*n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
*Find two lines, which together with x-axis forms a container, such that the container contains the most water.
*/
/*explaination:
Start by evaluating the widest container, using the first and the last line.
All other possible containers are less wide, so to hold more water, they need to be higher.
Thus, after evaluating that widest container, skip lines at both ends that don't support a higher height.
Then evaluate that new container we arrived at. Repeat until there are no more possible containers left.
*/
int maxArea(int* height, int heightSize) {
    int i = 0;
    int j = heightSize - 1;
    int water = 0;

    while(i < j){
        int h = height[i] < height[j]? height[i]:height[j];
        int w = h * (j-i);
        water = w > water? w:water;
        while(height[i] <= h && i<j) i++;
        while(height[j] <= h && i<j) j--;
    }
    return water;
}
