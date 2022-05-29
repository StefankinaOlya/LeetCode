class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answ = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    answ += 1
        return answ
