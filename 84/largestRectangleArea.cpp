/*递增序列，计算波峰的数值*/
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        if(height.size() == 0) return 0;
        stack<int> st;
        int MAX = 0;
        height.push_back(0);
        int area = 0;
        for(int i = 0; i < height.size(); ++i){
            while(!st.empty() && height[st.top()] > height[i]){
                int tmp = st.top();
                st.pop();
                area = (st.empty()? i:i-st.top()-1)*height[tmp];
                if(area > MAX) MAX = area;
            }
            st.push(i);
        }
        return MAX;
    }
};
