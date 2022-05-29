class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answ= 0 
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                answ += 1
        return answ
