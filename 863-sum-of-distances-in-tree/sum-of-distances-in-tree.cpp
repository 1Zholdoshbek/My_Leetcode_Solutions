class Solution {
public:
    int dfs1(int val,int par,vector<int>adj[],vector<int>&subtree){
        int curr=0;
        for(auto u:adj[val]){
            if(u!=par){
                curr+=dfs1(u,val,adj,subtree);
                curr+=subtree[u];
                subtree[val]+=subtree[u];
            }
        }
        return curr;
    }
    void dfs2(int v,int par,vector<int>adj[],vector<int>&ans,vector<int>&subtree,int now){
        ans[v]=now;
        for(auto u:adj[v]){
            if(u!=par){
                dfs2(u,v,adj,ans,subtree,now-subtree[u]+subtree[0]-subtree[u]);
            }
        }
    }
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
       vector<int>adj[n];
       vector<int>subtrees(n,1);vector<int>ans(n,0);
       for(int i=0;i<n-1;i++){
           adj[edges[i][0]].push_back(edges[i][1]);
           adj[edges[i][1]].push_back(edges[i][0]);
       }
      int root_sum=dfs1(0,-1,adj,subtrees);
      dfs2(0,-1,adj,ans,subtrees,root_sum);
      return ans;
    }
};