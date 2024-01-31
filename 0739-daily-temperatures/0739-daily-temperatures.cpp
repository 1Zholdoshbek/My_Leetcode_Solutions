class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n=temperatures.size();
        vector<int> result(n,0);
        int i=1;
        stack<int> st;
        st.push(0);
        while(!st.empty()){
            if(i>=n)
                break;
            if(temperatures[i]<=temperatures[st.top()]){
                st.push(i);
                i++;
            }else{
                result[st.top()]=i-st.top();
                st.pop();
                if(st.empty()){
                    st.push(i);
                    i++;
                }
            }
        }
    return result;        
    }
};