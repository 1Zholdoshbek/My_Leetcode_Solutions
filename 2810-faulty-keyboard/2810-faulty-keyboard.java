class Solution {
      public String reverseString(String name){
            StringBuilder k = new StringBuilder(); 
            k.append(name);
            k.reverse();
            return k.toString();
        } 
    public String finalString(String s) {
        String ans="";
        String p="";
        for(int i=0;i<s.length();i++){
            p+=s.charAt(i);
            if(s.charAt(i)=='i'){
                p=reverseString(p);
            }
        }
        for(int i=0;i<p.length();i++){
            if(p.charAt(i)=='i')
                continue;
            ans+=p.charAt(i);
        }
        return ans;
    }
}