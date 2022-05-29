class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answ = -1
        for i in range(len(nums)):
            if nums[i] == target:
                answ = i
        return answ
