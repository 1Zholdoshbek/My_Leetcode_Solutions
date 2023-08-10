class Solution {
    public int maximumXOR(int[] nums) {
        int tmp=0;
        
        for(int i:nums)
            tmp|=i;
        return tmp;
}
}
