class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        chislo = 0
        answ = []
        for i in range(len(digits)):
            chislo += (10 ** (len(digits) - i - 1)) * digits[i]
        for i in (list(str(chislo + 1))):
            answ.append(int(i))
        return answ
