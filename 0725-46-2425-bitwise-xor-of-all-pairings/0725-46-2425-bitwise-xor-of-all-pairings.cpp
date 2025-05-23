class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n1=nums1.size(), n2=nums2.size();
        unordered_map<int,long>freq;
        for(int n:nums1) freq[n]+=n2;
        for(int n:nums2) freq[n]+=n1;
        int res=0;
        for(auto& [n,c]:freq){
            if(c%2==1) res^=n;
        }
        return res;
    }
};