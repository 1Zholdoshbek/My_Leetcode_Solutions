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
            ans+=s.charAt(i);
            if(s.charAt(i)=='i'){
                ans=reverseString(ans);
            }
        }
        for(int i=0;i<ans.length();i++){
            if(ans.charAt(i)=='i')
                continue;
            p+=ans.charAt(i);
        }
        return p;
    }
}