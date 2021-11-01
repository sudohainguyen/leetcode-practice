class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        mid = n // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            sub_idx = self.search(nums[mid + 1:], target)
            if sub_idx != -1:
                return mid + sub_idx + 1
            else:
                return -1
