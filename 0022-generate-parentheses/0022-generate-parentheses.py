class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def Gen(left,right,s):
            if len(s)==n*2:
                ans.append(s)
                return 
            if left<n:
                Gen(left+1,right,s+'(')
            if right<left:
                Gen(left,right+1,s+')')
        ans=[]
        Gen(0,0,'')
        return ans
                
        