class Solution {
public:
    int findTheWinner(int n, int k) {
        vector<int>arr;
        for(int i=1;i<n+1;i++)
            arr.push_back(i);
        int tmp=0;
        while(arr.size()>1){
            tmp=(tmp+k-1)%arr.size();
            arr.erase(arr.begin()+tmp);
            
        }
        return arr[0];
    }
};