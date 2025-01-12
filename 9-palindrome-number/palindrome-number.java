class Solution {

    public static String reverse(String x){

        String y = "";
        for(int i=x.length()-1;i>=0;i--){
            y += x.charAt(i);
        }
        return y;
    }
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);

        if(s.equals(reverse(s))){
           return true;
        }
        else{
            return false;
        }
        
    }
}