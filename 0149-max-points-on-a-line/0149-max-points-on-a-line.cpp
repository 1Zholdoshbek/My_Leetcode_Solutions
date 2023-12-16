class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        if(points.size() == 1) return 1;
        int ans = 0;
        for(auto &it : points){
            unordered_map<double,int> mp;
            double x1 = it[0], y1 = it[1];
            for(auto &i : points){
                if(i == it) continue;
                double x2 = i[0], y2 = i[1];
                double curr_slope;
                if(x2-x1 == 0){
                    curr_slope = 1e9; // if line is vertical 
                }else{
                    curr_slope = (y2-y1)/(x2-x1);   
                }
                mp[curr_slope]++;
                ans = max(ans,mp[curr_slope]);
            }
        }
        return ans+1;
    }
};