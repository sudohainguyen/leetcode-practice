class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c not in pairs.keys():
                st.append(c)
            else:
                if len(st) == 0 or st[-1] != pairs[c]:
                    return False
                st.pop()
        return len(st) == 0