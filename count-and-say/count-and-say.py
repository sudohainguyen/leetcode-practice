class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.recursive(self.countAndSay(n - 1))
    
    def recursive(self, num: str):
        res = ""
        current = num[0]
        count = 1
        temp = f'{count}{current}'
        if len(num) == 1:
            return temp
        for c in num[1:]:
            if c != current:
                res = f'{res}{temp}'
                current = c
                count = 0
            count += 1
            temp = f'{count}{current}'
        return f'{res}{temp}'