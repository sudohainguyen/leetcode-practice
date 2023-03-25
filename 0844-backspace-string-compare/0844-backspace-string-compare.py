class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0
        len_s = len(s)
        _s = []
        len_t = len(t)
        _t = []
        while i < max(len_s, len_t):
            if i < len_s:
                if s[i] != '#':
                    _s.append(s[i])
                elif _s:
                    _s.pop()
            if i < len_t:
                if t[i] != '#':
                    _t.append(t[i])
                elif _t:
                    _t.pop()
            i += 1
        while _s and _t:
            if _s.pop() != _t.pop():
                return False
        return not _s and not _t
                