class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        half_x = x // 2
        prev_x = x
        while True:
            if half_x ** 2 <= x and (half_x + 1) ** 2 > x:
                return half_x
            if half_x ** 2 > x:
                prev_x = half_x
                half_x = half_x // 2
            else:
                half_x = (prev_x + half_x) // 2