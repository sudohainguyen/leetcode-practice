import math
class Solution:
    memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        count = 1
        num_two = n // 2
        for i in range(num_two):
            freq_two = i + 1
            num_one = n - freq_two * 2
            count += math.comb(freq_two + num_one, freq_two)
        return count
