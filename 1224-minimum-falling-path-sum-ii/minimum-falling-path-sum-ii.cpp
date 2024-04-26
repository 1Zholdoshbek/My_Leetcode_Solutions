class Solution {
public:
  int minFallingPathSum(vector<vector<int>>& arr) {
    constexpr int kInf = 1e6;
    for (int i = 1; i < arr.size(); ++i)
      for (int j = 0; j < arr[0].size(); ++j) {
        int m = kInf;
        for (int k = 0; k < arr[0].size(); ++k) {
          if (k == j) continue;
          m = min(m, arr[i - 1][k]);
        }
        arr[i][j] += m;
    }
    return *min_element(begin(arr.back()), end(arr.back()));
  }
};