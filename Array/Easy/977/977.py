class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answ = []
        for i in nums:
            answ.append(i ** 2)
        return sorted(answ)
