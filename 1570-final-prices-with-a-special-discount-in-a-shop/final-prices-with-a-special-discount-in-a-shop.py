class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=[]
        tmp=[0]
        for i in prices[::-1]:
            while i<tmp[-1]:tmp.pop()
            res+=[i-tmp[-1]]
            tmp.append(i)
        return res[::-1]
        