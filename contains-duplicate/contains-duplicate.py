class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_unique = len(set(nums))
        return len_unique != len(nums)