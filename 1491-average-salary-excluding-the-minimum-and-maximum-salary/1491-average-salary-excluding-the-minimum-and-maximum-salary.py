class Solution:
    def average(self, salary: List[int]) -> float:
        sorted_sal = sorted(salary)
        return sum(sorted_sal[1:-1]) / (len(salary) - 2)