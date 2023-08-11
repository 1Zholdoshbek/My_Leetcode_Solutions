class Solution {
    public int countDistinctIntegers(int[] nums) {
        
        Set<Integer>myset = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            myset.add(nums[i]);
            String tmp = new StringBuilder(nums[i]+"").reverse().toString();
            myset.add(Integer.valueOf(tmp));
        }
        return myset.size();
    }
}