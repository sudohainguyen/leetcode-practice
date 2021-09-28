class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: 
            return
        if m == 0:
            nums1[:] = nums2[:]
            return
        i = m - 1
        j = n - 1
        total = m + n
        while i >= 0 and j >= 0:
            total -= 1
            if nums1[i] > nums2[j]:
                nums1[total] = nums1[i]
                i -= 1
            else:
                nums1[total] = nums2[j]
                j -= 1
        if i == -1:
            nums1[:j + 1] = nums2[:j + 1]
        
        