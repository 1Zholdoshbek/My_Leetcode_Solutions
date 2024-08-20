class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=str(x)
        sum=0
        for i in s:
            sum+=int(i)
        if x%sum==0:
            return sum
        return -1
            