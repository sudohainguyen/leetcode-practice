class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)
        if len_w1 == 0 and len_w1 == len_w2 or word1 == word2:
            return 0
        
        d = [[0 for i in range(len_w2 + 1)] for j in range(len_w1 + 1)]
        d[0][0] = 0
        for i in range(1, len_w1 + 1):
            d[i][0] = i
        for j in range(1, len_w2 + 1):
            d[0][j] = j
        for i in range(1, len_w1 + 1):
            for j in range(1, len_w2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min([d[i-1][j], d[i][j-1], d[i-1][j-1]]) + 1
        return d[len_w1][len_w2]