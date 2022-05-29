class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answ = [0]
        for i in range(len(gain)):
            answ.insert(i, answ[i-1] + gain[i])
        return max(answ)
