class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n=grid.size(),repeat=-1;
        vector<int> result(n*n+1,0);
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(result[grid[i][j]])repeat=grid[i][j];
                else{
                    result[grid[i][j]]=true;
                }
            }
        }
        for(int i=1;i<=n*n;i++){
            if(!result[i])return {repeat,i};
        }
        return{};
    }
};