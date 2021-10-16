class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_1 = len(nums1)
        len_2 = len(nums2)
        result = []
        temp = {}
        if len_1 < len_2:
            for num in nums1:
                if num not in temp:
                    temp[num] = 0
                temp[num] += 1
            for num in nums2:
                if temp.get(num, 0) > 0:
                    temp[num] -= 1
                    result.append(num)
                    if len(result) == len_1:
                        break
        else:
            for num in nums2:
                if num not in temp:
                    temp[num] = 0
                temp[num] += 1
            for num in nums1:
                if temp.get(num, 0) > 0:
                    temp[num] -= 1
                    result.append(num)
                    if len(result) == len_2:
                        break
        return result