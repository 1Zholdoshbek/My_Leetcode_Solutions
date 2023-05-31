class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int sum=0;
        int l=nums.size()-1;
        int tmp=nums[l];
        for(int i=0;i<k;i++){
            sum+=tmp;
            tmp++;
        }
        return sum;
    }
};