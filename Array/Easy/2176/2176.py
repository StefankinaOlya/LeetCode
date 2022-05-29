class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        answ = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0 and i != j:
                    answ += 1
        return answ
