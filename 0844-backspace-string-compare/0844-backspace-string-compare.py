class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0
        len_s = len(s)
        _s = []
        len_t = len(t)
        _t = []
        while i < max(len_s, len_t):
            if i < len_s:
                if s[i] == '#':
                    if _s:
                        _s.pop()
                else:
                    _s.append(s[i])
            if i < len_t:
                if t[i] == '#':
                    if _t:
                        _t.pop()
                else:
                    _t.append(t[i])
            i += 1
        return ''.join(_s) == ''.join(_t)
                