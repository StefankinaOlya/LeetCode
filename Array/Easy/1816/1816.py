class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        answ = ""
        for i in s.split()[:k]:
            answ += str(i) + " "
        return answ[:-1]
