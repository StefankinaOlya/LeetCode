class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answ = []
        for i in range(1, len(nums) + 1):
            answ.append(sum(nums[:i]))
        return answ
