class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int longestSize = 0;        
        unordered_map <char, bool> checkedLetter;   
        for (int start = 0, end = 0; start < s.length() && end < s.length();) {
            if (checkedLetter[s[end]] == false) {
                checkedLetter[s[end]] = true;
                end = end + 1;
                longestSize = max(longestSize, end-start);
            } else {
                checkedLetter[s[start]] = false;
                start = start + 1;
            }
        }
        return longestSize;
    }
};