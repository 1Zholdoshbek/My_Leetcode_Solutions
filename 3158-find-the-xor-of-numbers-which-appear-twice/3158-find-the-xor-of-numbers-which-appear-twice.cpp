class Solution {
public:
    int duplicateNumbersXOR(vector<int>& nums) {
        unordered_set<int>sets;
        int ans=0;
        for(int i:nums){
            if(sets.find(i)!=sets.end(i)) ans^=i;
            else sets.insert(i);
        }
        return ans;
    }
};