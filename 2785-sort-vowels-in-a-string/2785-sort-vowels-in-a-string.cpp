class Solution {
public:
    string sortVowels(string s) {
        vector<int>pos;
        vector<char>val;
        for(int i=0;i<s.size();i++){
            if(s[i]=='a' || s[i]=='A' || s[i]=='E' || s[i]=='u' || s[i]=='U'||s[i]=='e' || s[i]=='o' || s[i]=='O' || s[i]=='i' || s[i]=='I'){
                pos.push_back(i);
                val.push_back(s[i]);
            }
            
        }
        sort(val.begin(),val.end());
        for(int i=0;i<pos.size();i++){
            s[pos[i]]=val[i];
        }
        return s;
    }
};