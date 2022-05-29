class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answ = []
        for i in range(len(nums)):
            answ.insert(i, nums[nums[i]])
        return answ
