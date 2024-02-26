class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        int data[101]={0};
        for(int i=0;i<nums.size();i++){
            data[nums[i]]++;
            if(data[nums[i]]>2)return false;
        }
        return true;
    }
};