class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int tmp=0,m=0,p=0,g=0;
        for(int i=0;i<garbage.size();i++){
            for(int j=0;j<garbage[i].size();j++){
                tmp++;
                if('M'==garbage[i][j])m=i;
                else if('P'==garbage[i][j])p=i;
                else if('G'==garbage[i][j])g=i;
            }
        }
        for(int i=0;i<travel.size();i++){
            if(m-1>=i)tmp+=travel[i];
            if(p-1>=i)tmp+=travel[i];
            if(g-1>=i)tmp+=travel[i];
        }
        return tmp;
        
    }
};