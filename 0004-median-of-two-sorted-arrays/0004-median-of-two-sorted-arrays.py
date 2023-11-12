class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        
        if len(nums1) % 2 == 0:
            n = len(nums1) // 2
            return (nums1[n - 1] + nums1[n]) / 2
        else:
            n = (len(nums1) // 2) + 1
            return nums1[n - 1]