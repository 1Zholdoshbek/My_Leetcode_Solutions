class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        vector<bool> visited(n, false);
        int completeCount = 0;

        for (int i = 0; i < n; ++i) {
            if (visited[i]) continue;

            queue<int> q;
            unordered_set<int> component;
            q.push(i);
            visited[i] = true;
            component.insert(i);

            while (!q.empty()) {
                int curr = q.front(); q.pop();
                for (int neighbor : graph[curr]) {
                    if (!component.count(neighbor)) {
                        component.insert(neighbor);
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }

            bool isComplete = true;
            for (int node : component) {
                if (graph[node].size() != component.size() - 1) {
                    isComplete = false;
                    break;
                }
            }

            if (isComplete) completeCount++;
        }

        return completeCount;
    }
};