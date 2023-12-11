class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt=0
        cnt2=0
        for i in nums1:
            for j in nums2:
                if i==j:
                    cnt+=1
                    break
        for i in nums2:
            for j in nums1:
                if i==j:
                    cnt2+=1
                    break
        return [cnt,cnt2]
        
        