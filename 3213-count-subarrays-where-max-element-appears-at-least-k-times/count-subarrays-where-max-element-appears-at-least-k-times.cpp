class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long left=0,right=0,ans=0;
        long long n=nums.size();
        long long maxi=*max_element(nums.begin(),nums.end());
        long long count=0;
       

        while(right<n){
            if(nums[right]==maxi) count++;
            if(count>=k){
                while(count>=k){
                    ans+=n-right;
                    if(nums[left]==maxi) count--;
                    left++;
                }
                
            }
            right++;         
        }
        return ans;
    }
};