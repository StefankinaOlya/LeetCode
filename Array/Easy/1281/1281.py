class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        proz, summa = 1, 0
        n_str = list(str(n))
        for i in n_str:
            proz *= int(i)
            summa += int(i)
        return proz - summa
