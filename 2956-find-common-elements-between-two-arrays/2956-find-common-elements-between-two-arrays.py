class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        cnt1=sum(1 for i in nums1 if i in set2)
        cnt2=sum(1 for i in nums2 if i in set1)
        return [cnt1,cnt2]
        