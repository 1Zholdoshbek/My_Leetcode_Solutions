class Solution {
    public int differenceOfSums(int n, int m) {
    int tmp1=0,tmp2=0;
        for(int i=1;i<=n;i++){
            if(i%m!=0){
                tmp1+=i;
            }
            else{
                tmp2+=i;
            }
        }
        return tmp1-tmp2;
        
    }
}