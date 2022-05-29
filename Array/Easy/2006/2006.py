class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        answ = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k and i != j:
                    print(i, j, nums[i], nums[j])
                    answ += 1
        return answ
