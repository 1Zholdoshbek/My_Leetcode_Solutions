class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<int> ans(2, -1);
        int prime1 = 0, minDif = 10000000;
        for (int i = left; i <= right; i++) {
            if (i == 1) {
                continue;
            }
            bool isPrime = !(i % 2 == 0 && i > 2);
            if (isPrime) {
                for (int j = 2; j * j <= i; j++) {
                    if (i % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
            }
            if (!isPrime) {
                continue;
            }
            if (prime1 != 0 && i - prime1 < minDif) {
                minDif = i - prime1;
                ans = {prime1, i};
                if (minDif <= 2) {
                    return ans;
                }
            }
            prime1 = i;
        }
        return ans;
    }
};