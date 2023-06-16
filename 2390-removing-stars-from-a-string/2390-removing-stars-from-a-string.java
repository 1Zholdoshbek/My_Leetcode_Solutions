class Solution {
    public String removeStars(String s) {
        Stack<Character>mystack = new Stack<>();
        StringBuilder res = new StringBuilder();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='*'){
                mystack.pop();
            }
            else{
                mystack.push(s.charAt(i));
            }
        }
        while(!mystack.isEmpty()){
            res.append(mystack.pop());
        }
        return res.reverse().toString();
    }
}