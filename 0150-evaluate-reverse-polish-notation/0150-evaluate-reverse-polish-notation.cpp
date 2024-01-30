class Solution {
public:
    int evalRPN(vector<string>& t) {
        stack<int> st;
        for(int i=0; i<t.size(); i++) {
            if(t[i]=="+"||t[i]=="-"||t[i]=="/"||t[i]=="*") {
                int a,b,c;
                a = st.top();
                st.pop();
                b = st.top();
                st.pop();
                if(t[i]=="+") c = a+b;
                else if(t[i]=="*") c = a*b;
                else if(t[i]=="-") c = b-a;
                else c = b/a;
                st.push(c);
            }else st.push(stoi(t[i]));     
        }
        return st.top();
    }
};