class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int i=0,j=0;
        sort(s.begin(),s.end());
        sort(g.begin(),g.end());
        while(i<s.size() && j<g.size()){
            if (s[i]>=g[j])j+=1;
            i+=1;
        }
        return j;
    }
};