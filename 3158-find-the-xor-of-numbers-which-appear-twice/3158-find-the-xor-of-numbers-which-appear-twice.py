class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        sets=set(nums)
        if len(nums)==len(sets):
            return 0
        else:
            nums.sort()
            l=[]
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]==nums[j]:
                        l.append(nums[i])
            print(l)
            ans=0
            if len(l)==1:
                return l[0]
            for i in l:
                ans^=i
            return ans
        