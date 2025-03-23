class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> graph(n);
        for (const auto& r : roads){
            int u = r[0], v = r[1], time = r[2];
            graph[u].push_back({v, time});
            graph[v].push_back({u, time});
        }
        const int MOD = 1e9 + 7;
        vector<long long> distance(n, LLONG_MAX);
        vector<long long> count(n, 0);
        distance[0] = 0;
        count[0] = 1;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        pq.push({0, 0});
        
        while (!pq.empty()){
            auto [curr_dist, u] = pq.top();
            pq.pop();
            if (curr_dist > distance[u])
                continue;
            for (const auto& nei : graph[u]){
                int v = nei.first, time = nei.second;
                long long new_path =curr_dist + time;
                if (new_path < distance[v]){
                    distance[v] = new_path;
                    count[v] = count[u];
                    pq.push({new_path, v});
                }
                else if (new_path == distance[v]){
                    count[v] = (count[v] + count[u]) % MOD;
                }
            }
        }
        return count[n - 1];
    }
};
