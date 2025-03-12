class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int maxx=0,min=0;
        for(int i:nums){
            if(i>0)maxx++;
            else if(i<0)min++;
        }
        if(maxx>min)return maxx;
        else return min;
    }
};