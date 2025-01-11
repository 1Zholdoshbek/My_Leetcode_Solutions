class Solution {
public:
    bool canConstruct(string s, int k) {
        int n = s.size();
        if (n < k) return 0;
        vector<int> v(26, 0);
        for (auto& i : s) v[i - 'a']++;

        int odd = 0;
        for (auto& i : v){
            if (i % 2) odd++;
        }  
        if(odd>k)return 0;
        return 1;
    }
};