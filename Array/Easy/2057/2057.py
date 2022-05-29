class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        answ = -1
        answer = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                answer.append(i)
        if len(answer) > 0:
            return min(answer)
        return answ
