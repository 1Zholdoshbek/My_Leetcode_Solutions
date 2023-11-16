class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int n =releaseTimes.length;
        int firstElem=releaseTimes[0];
        char a = keysPressed.charAt(0);
        for(int i=1;i<n;i++){
            int tmp = releaseTimes[i]-releaseTimes[i-1];
            if(tmp>firstElem ||(tmp==firstElem && keysPressed.charAt(i)>a)){
                firstElem=tmp;
                a=keysPressed.charAt(i);
            }
        }
        return a;
    }
}