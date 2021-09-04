class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        if len(strs) == 1:
            return first
        found = False
        i = 0
        while i < len(first) and not found:
            for s in strs[1:]:
                if i == len(s) or s[i] != first[i]:
                    found = True
                    i -= 1
                    break
            i += 1
        return first[:i]