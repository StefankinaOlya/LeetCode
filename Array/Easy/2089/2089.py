class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums1 = sorted(nums)
        answ = []
        for i in range(len(nums1)):
            if nums1[i] == target:
                answ.append(i)
        return answ
