class Solution {
    
   public int ReverseNumber(int i){
       int sum=0;
       while(i>0){
           sum=sum*10+(i%10);
           i/=10;
       }
       return sum;
   }
    public int countDistinctIntegers(int[] nums) {
        Set<Integer>myset =  new HashSet<>();
        for(int i:nums){
            myset.add(i);
            myset.add(ReverseNumber(i));
            
        }
        return myset.size();
    }
}