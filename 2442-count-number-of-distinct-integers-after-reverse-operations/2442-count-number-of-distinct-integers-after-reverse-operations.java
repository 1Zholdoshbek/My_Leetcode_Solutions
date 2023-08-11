class Solution {
    public int countDistinctIntegers(int[] nums) {
        
        HashSet<Integer>myset = new HashSet<>();
        for(int i:nums)
            myset.add(i);
        
        for(int i=0;i<nums.length;i++){
            String tmp="";
            StringBuilder strb = new StringBuilder();
            
            tmp=Integer.toString(nums[i]);
            strb.append(tmp);
            strb.reverse();
            
            myset.add(Integer.parseInt(strb.toString()));
      }
        
        return myset.size();
        
    }
}