class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True
        cnt = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt == 2:
                    return False
        if nums[-1] > nums[0] and cnt == 1:
            return False
        return True
            