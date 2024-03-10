class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> st;
        vector<int> ans;

        for (auto it : nums1) {
            st.insert(it);
        }

        for (auto it : nums2) {
            if (st.count(it)) {
                ans.push_back(it);
                st.erase(it);  // Remove the element from the set to avoid duplicates
            }
        }

        return ans;
    }
};