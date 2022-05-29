class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        chet = 0
        answ = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    chet += 1
            answ.append(chet)
            chet =  0
        return answ
