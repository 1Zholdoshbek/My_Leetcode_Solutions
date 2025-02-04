class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int currentSum = nums[0], maxSum = currentSum;
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i - 1]) {
                currentSum += nums[i]; // Extend ascending subarray
            } else {
                currentSum = nums[i]; // Start new subarray
            }
            maxSum = max(maxSum, currentSum); // Update max sum
        }
        
        return maxSum;
    }
};