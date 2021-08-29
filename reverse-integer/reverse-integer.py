class Solution:
    def reverse(self, x: int) -> int:
        cur_num = 0
        is_neg = -1  if x < 0 else 1
        x = abs(x)
        while x != 0:
            cur_num = cur_num * 10 + x % 10
            if cur_num > 2 ** 31 - 1 or cur_num < -2 ** 31:
                return 0
            x = x // 10
        return cur_num * is_neg