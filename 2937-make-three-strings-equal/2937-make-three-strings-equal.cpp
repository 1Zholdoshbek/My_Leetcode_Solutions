class Solution {
public:
    int findMinimumOperations(string s1, string s2, string s3) {
        int i=0,j=0,k=0;
        while(i<s1.size() && j<s2.size() && k<s3.size()){
            if(s1[i]==s2[j] && s2[j]==s3[k]){
                i++;
                j++;
                k++;
            }
            else break;
            
        }
        if(!i || !j || !k) return -1;
        return (s1.size()-i)+(s2.size()-j)+(s3.size()-k);
    }
};