class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        i, j = 0, 0
        prev = nums[0]
        while i < n and j < n:
            if nums[j] > nums[i]:
                i += 1
                nums[i] = nums[j]
                
            j += 1
        return i + 1
