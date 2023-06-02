class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        right=0
        left=len(s)-1
        ans=[i for i in s]
        while right<=len(s)/2:
            ans[right]=min(ans[right],ans[left])
            ans[left]=ans[right]
            right+=1
            left-=1
        return "".join(ans)
            
