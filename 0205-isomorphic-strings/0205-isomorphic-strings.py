class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        i = 0
        l = len(s)
        while i < l:
            s_char = s[i]
            t_char = t[i]
            _s = s_to_t.get(s_char, None)
            if _s:
                if _s != t_char:
                    return False
            else:
                s_to_t[s_char] = t_char
            
            _t = t_to_s.get(t_char, None)
            if _t:
                if _t != s_char:
                    return False
            else:
                t_to_s[t_char] = s_char
            i += 1
        return True
