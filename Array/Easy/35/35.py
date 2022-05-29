class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        for i in range(len(nums)):
            if nums[i] == target:
                answer = i
        return answer
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = self.search(nums, target)
        if answer == -1:
            nums.append(target) 
            answer = self.search(sorted(nums), target)
        return answer
