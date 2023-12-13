class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int cnt=0,o=capacity;
        for(int i=0;i<plants.size();i++){
            if(o<plants[i]){
                cnt+=2*i;
                o=capacity;
            }
            cnt++;
            o-=plants[i];
        }
        return cnt;
        
    }
};