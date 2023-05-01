class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        max = 1000
        min = 1e6
        for item in salary:
            if item < min:
                min = item
            if item > max:
                max = item
            
            total += item

        return (total - max - min) / (len(salary) - 2)

