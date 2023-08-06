class Solution {
    public String finalString(String s) {
        StringBuilder ans = new StringBuilder();
        for(char c:s.toCharArray()){
            if(c=='i')
                ans.reverse();
            else
                ans.append(c);
        }
        return ans.toString();
        
    }
}