class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int tmp=0,ans=0;
        for(auto i:nums){
            tmp+=i;
            ans=min(ans,tmp);
        }
        return abs(ans)+1;
    }
};