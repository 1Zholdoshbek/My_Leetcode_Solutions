class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        long long n = nums.size();
        if(n<=2) return 0;

        long long ans = 0 ; 
        unordered_map<long long,long long> dp[n+1];
        for(long long i = 1 ; i < n ; i++){
            for(long long j = 0 ; j<i ; j++){
                long long cnt = 1;
                long long diff = (long long)nums[i]-(long long)nums[j];

                // agr diff ke sath ek length alredy present hai to
                if(dp[j].count(diff)){
                   cnt = dp[j][diff];
                   dp[i][diff]+= cnt;
                   ans += cnt;
                }

                dp[i][diff] += 1 ;  // 1 + to add curr element
            }
        }
        return ans;
        
    }
};