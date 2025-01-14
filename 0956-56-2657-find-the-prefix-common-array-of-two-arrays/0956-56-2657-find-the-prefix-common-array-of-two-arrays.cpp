class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        vector<int> common(n);
        vector<int> freq1(51), freq2(51);

        for (int i = 0; i < n; i++) {
            int a = A[i], b = B[i];
            freq1[a]++;
            freq2[b]++;
            for (int j = 0; j < 51; j++) {
                if (freq1[j] == freq2[j] && freq1[j] != 0) {
                    common[i]++;
                }
            }
        }
        return common;
    }
};