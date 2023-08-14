class Solution {
    public int maxSum(int[] nums) {
        int ans=-1;
        for(int i=0;i<nums.length;i++){
              String  c = String.valueOf(nums[i]);
            char[] s = c.toCharArray();
            Arrays.sort(s);
            
            for(int j=i+1;j<nums.length;j++){
                String  c2 = String.valueOf(nums[j]);
            char[] s2 = c2.toCharArray();
            Arrays.sort(s2);
                if(s[s.length-1]==s2[s2.length-1]){
                    ans=Math.max(ans,(nums[i]+nums[j]));
                }
            }
        }
        
 return ans;
    }
}