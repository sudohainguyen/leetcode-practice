class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s == 0:
            return True
        elif len_t == 0:
            return False
        i = 0
        j = 0
        while len_t - j >= len_s - i and j < len_t:
            if s[i] == t[j]:
                i += 1
            if i == len_s:
                return True
            j += 1
        return False