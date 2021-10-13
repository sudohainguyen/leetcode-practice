class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current, result = nums[0], nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i] )
            result = max(current, result)
        return result