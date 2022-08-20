class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        mid = n // 2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            if n == 1:
                return 0
            return self.searchInsert(nums[:mid], target)
        if nums[mid] < target:
            if n == 1:
                return mid + 1
            return mid + self.searchInsert(nums[mid:], target)
        