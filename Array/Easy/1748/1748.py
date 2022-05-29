class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summa = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                summa += nums[i]
        return summa
