class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left =0
        right=len(s)-1
        ans=[]
        ans.extend(s)
        while left<=len(s)/2:
            ans[left]=min(ans[right],ans[left])
            ans[right]=ans[left]
            left+=1
            right-=1
        print(ans)
        return "".join(ans)
            
