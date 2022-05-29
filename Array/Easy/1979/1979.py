class Solution:
    def findGCD(self, nums: List[int]) -> int:
        answ = 1
        for i in range(answ, max(nums) +1):
            if min(nums) % i == 0 and max(nums) % i == 0:
                answ = i
        return answ
